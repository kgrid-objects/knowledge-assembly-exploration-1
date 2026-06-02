import pgx from 'pgx-ka/all-recommendation-library';

// define the item component
Vue.component('recomtile', {
  template: '#recomtile-template',
  props: [
    'recmodel',
    'reckey',
    'recindex',
    'library_url', 
    'recsource'
  ],
  data: function () {
    return {
      reclabel: { genes: "Based on", classification: "Classification of recommendations", content: "Dosing recommendations", implication: "Implications for phenotypic measures" }
    }
  },
  computed: {
    recrender: function () {
      var obj = {}
      var phenovalue = ''
      for (var key in this.recmodel.result.genes) {
        if (phenovalue != '') {
          phenovalue = phenovalue + " "
        }
        if (this.recmodel.result.genes[key].phenotype) {
          if (this.recmodel.result.genes[key].phenotype != '') {
            phenovalue = phenovalue + key + " " + this.recmodel.result.genes[key].phenotype
          }
        } else {
          if (this.recmodel.result.genes[key].diplotype != '') {
            phenovalue = phenovalue + key + " " + this.recmodel.result.genes[key].diplotype
          }
        }
      }
      obj.genes = phenovalue
      obj.classification = this.recmodel.result.recommendation.classification
      obj.implication = this.recmodel.result.recommendation.implication
      obj.content = this.recmodel.result.recommendation.content
      return obj
    },
    objlink: function () {
      return `https://kgrid-objects.github.io/pgx-knowledge-assembly/${this.recsource}_${this.reckey}.html`;
    }
  }
})

// boot up the demo
var demo = new Vue({
  el: '#app',
  data: function () {
    return {
      initdata: {},
      isLogOpen: false,
      logSectionTitle: '',
  currentView: '',
      autofillSelection: '',
      eventlog: [],
      delay: 1500,
      logtext: { 'request': 'K-GRID Service Request - Sending request to Knowledge Object ark:', 'response': '' },
      patientsamples: [],
      phenotypePanel: {},
      diplotypePanel: {},
      recommendationlistks2: [],
      recommendationlistks3: [],
      activeTab: 'assembly',
      chatbotUrl: 'https://llmchatbot-d6e6fdd6b02f.herokuapp.com/',
      assemblyUrl: 'https://kgrid-objects.github.io/pgx-knowledge-assembly/pgx_ka_info_page.html'
    }
  },
  created: function () {
    var self = this
    axios.all([
      axios.get('./static/json/initdata.json'),
      axios.get('./static/json/config.json')
    ]).then(axios.spread(function (initresp, config) {
      self.appendLog('app', 'Application Event - Loading Configuration...')
      self.appendLog('app', 'Application Event - Loading Initial Data...')
      self.initdata = initresp.data
      self.patientsamples = initresp.data.patientsamples
      self.phenotypePanel = JSON.parse(JSON.stringify(initresp.data.initrequest.diplotype))
      self.diplotypePanel = JSON.parse(JSON.stringify(initresp.data.initrequest.diplotype))

    })).catch(function (error) {
      console.log(error)
    })
  },
  computed: {
    debouncegetdata: function () {
      return _.debounce(this.getdata, this.delay)
    }
    ,
    rawDataJson: function() {
      try {
        return JSON.stringify({ diplotype: this.diplotypePanel }, null, 2)
      } catch (e) {
        return '{}'
      }
    },
    rawOutputJson: function() {
      try {
        return JSON.stringify({ phenotypePanel: this.phenotypePanel, recommendationlistks2: this.recommendationlistks2, recommendationlistks3: this.recommendationlistks3 }, null, 2)
      } catch (e) {
        return '{}'
      }
    }
  },
  watch: {
    autofillSelection: function () {
      var self = this
      if (this.autofillSelection != '') {
        this.delay = 200
        var i = parseInt(this.autofillSelection)
        window.setTimeout(function () {
          self.autofill(i)
        }, 50)
        this.appendLog('app', 'Application Event - Autofill Sample #' + i + ' is selected.')
      }
    },
    diplotypePanel: {
      handler: function (after, before) {
        var ready = false
        var self = this
        this.resetapp()
        for (var key in this.diplotypePanel) {
          ready = ready || (this.diplotypePanel[key] != '')
        }
        if (ready) {
          this.debouncegetdata()
        }
      },
      deep: true
    }
  },
  methods: {
    showLogSection: function(title) {
      // map incoming titles to internal view names
      var view = ''
      if (title === 'LOG') {
        view = 'LOG'
        this.logSectionTitle = 'PGX Demo APP LOG'
      } else if (title === 'SEE RAW DATA') {
        view = 'RAW_DATA'
        this.logSectionTitle = 'RAW DATA'
      } else if (title === 'SEE RAW OUTPUT') {
        view = 'RAW_OUTPUT'
        this.logSectionTitle = 'RAW OUTPUT'
      } else {
        view = title
        this.logSectionTitle = title
      }
      // set the current view and open the collapse
      this.currentView = view
      this.isLogOpen = true
      // scroll to end only when viewing logs
      if (view === 'LOG') {
        var self = this
        this.$nextTick(function() {
          self.scrollToEnd()
        })
      }
    },
    copyContent: function() {
      var textToCopy = ''
      if (this.currentView === 'RAW_DATA') {
        textToCopy = this.rawDataJson
      } else if (this.currentView === 'RAW_OUTPUT') {
        textToCopy = this.rawOutputJson
      } else if (this.currentView === 'LOG') {
        // concatenate eventlog entries into a readable string
        textToCopy = this.eventlog.map(e => e.timestamp + ' - ' + e.text).join('\n')
      } else {
        textToCopy = this.logSectionTitle || ''
      }

      var self = this
      if (!textToCopy) {
        this.appendLog('app', 'Copy failed: nothing to copy')
        return
      }

      // preferred modern API
      if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(textToCopy).then(function() {
          self.appendLog('app', 'Copied content to clipboard')
        }).catch(function(err) {
          // fallback to execCommand
          try {
            var ta = document.createElement('textarea')
            ta.value = textToCopy
            ta.style.position = 'fixed'
            ta.style.left = '-9999px'
            document.body.appendChild(ta)
            ta.select()
            document.execCommand('copy')
            document.body.removeChild(ta)
            self.appendLog('app', 'Copied content to clipboard (fallback)')
          } catch (e) {
            self.appendLog('app', 'Copy failed: ' + (err && err.message ? err.message : e && e.message ? e.message : 'unknown'))
          }
        })
      } else {
        // older browsers
        try {
          var ta2 = document.createElement('textarea')
          ta2.value = textToCopy
          ta2.style.position = 'fixed'
          ta2.style.left = '-9999px'
          document.body.appendChild(ta2)
          ta2.select()
          document.execCommand('copy')
          document.body.removeChild(ta2)
          this.appendLog('app', 'Copied content to clipboard (fallback)')
        } catch (e) {
          this.appendLog('app', 'Copy failed: ' + (e && e.message ? e.message : 'unknown'))
        }
      }
    },
    appendLog: function (key, s) {
      var ts = moment().format('ddd, MMM Do YYYY, h:mm:ss A Z')
      var entry = {}
      entry.key = key
      entry.timestamp = ts
      entry.text = s
      this.eventlog.push(entry)
      this.scrollToEnd()
    },
    resetapp: function () {
      var self = this
      this.recommendationlistks2 = []
      this.recommendationlistks3 = []
      Object.keys(this.phenotypePanel).forEach(function (key) {
        self.phenotypePanel[key] = {}
      })
    },
    autofill: function (i) {
      this.resetapp()
      this.diplotypePanel = JSON.parse(JSON.stringify(this.patientsamples[i].diplotype))
    },
    scrollToEnd: function () {
      var container = this.$el.querySelector('#statuslog')
      container.scrollTop = container.scrollHeight
    },
    getdata: async function () {
      var self = this
      Object.keys(self.phenotypePanel).forEach(function (key) {
        self.phenotypePanel[key] = {}
      })
      try {
        const result = await pgx.run({
          "diplotype": self.diplotypePanel
        }
        );

        self.recommendationlistks2 = result.finalKS2
          .filter(item => typeof item === 'object' && item !== null)
          .map(item => ({ result: item }));
        self.recommendationlistks3 = result.finalKS3
          .filter(item => typeof item === 'object' && item !== null)
          .map(item => ({ result: item }));

        Object.keys(result.intermediate).forEach(function (key) {
          self.phenotypePanel[key] = result.intermediate[key]
        })
      } catch (err) {
        console.error('Fetch error:', err);
      }
    },
    openAssemblyLink() {
      window.open(this.assemblyUrl, '_blank', 'noopener');
    }
  }
})
