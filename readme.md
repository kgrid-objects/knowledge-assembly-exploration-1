# PGx Knowledge Assembly (PGx-KA)

### What is the PGx-KA?

The PGx-KA is a prototype pharmacogenomics "knowledge assembly" enabling general explorations into knowledge assembly construction.

Its formal architecture is an example Knowledge Object (KO) of the **Knowledge Assembly (KA) type**.

For this work, a **Knowledge Assembly** is a **distinct type** of KO that has one or more Knowledge Sets and one or more Purposes. (Note: A Knowledge Set is just an appropriately typed unordered list of KOs.) 

In keeping with this definition of a KA, the PGx-KA has the following three Knowledge Sets:

- Knowledge Set 1 (KS1): A list of KOs with implementations of knowledge for mapping genotypes to pharmacogenomic (PGx) phenotypes based on [CPIC guidelines](https://cpicpgx.org/guidelines/). KS1 can be found in the PGx-KA's [metadata file](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/metadata.json). 
- Knowledge Set 2 (KS2): A list of KOs with implementations of knowledge for mapping PGx phenotypes to drug-specific recommendations based on [CPIC guidelines](https://cpicpgx.org/guidelines/). KS2 can be found as an external release [here](https://raw.githubusercontent.com/kgrid-objects/pgx-knowledge-assembly/refs/tags/1.0/collection/drug_recommendation_knowledge_set/metadata.json).
- Knowledge Set 3 (KS3): A list of KOs with implementations of knowledge for mapping PGx phenotypes to drug-specific recommendations based on [DPWG guidelines](https://www.clinpgx.org/page/dpwg). KS3 can be found in the PGx-KA's [metadata file](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/metadata.json). 

The PGx-KA also has the following two quoted Purposes:

1. "To compute patient specific drug selection and dosing recommendations."
2. "To serve as an example of building a Knowledge Assembly by adopting and extending the properties and relationships defined for Knowledge Objects." 

These two Purposes meet with the definition of a Purpose for a KA from [NCIT](https://ontobee.org/ontology/NCIT?iri=http://purl.obolibrary.org/obo/NCIT_C25634), which is "what something is used for; reason or intention."   

The PGx-KA meets all of the requirements of a Knowledge Assembly type of Knowledge Object or "KA-KO." For more information about the formalized Knowledge Objects (KOs) we work with, see the Knowledge Object Implementation Ontology [here at Github](https://github.com/kgrid/koio) and [here at Bioportal](https://bioportal.bioontology.org/ontologies/KOIO). Note, as of September 2025, the terms Knowledge Assembly and Knowledge Set have NOT yet been added to KOIO as they are formative.

- - - 

### Who created the PGx-KA?

The PGx-KA is experimental work of the Knowledge Systems Lab (KSL) at the University of Michigan. For more details about our lab, see [KSL @ U-M](https://knowledge-systems.lab.medicine.umich.edu/).

- - - 

### What type of evidence-based computations does the PGx-KA support?

Disclaimer:  The PGx-KA is an experiment in knowledge assembly construction and NOT intended for production use.  The knowledge in PGx-KA may not be up to date or reliable.

The PGx-KA can be used to compute the following two things in sequence. First, it leverages computable implementations of knowledge to map an individual's genotype information for a group of 7 (SEVEN) genes that control the absorption, distribution, metabolism, and excretion of 29 (TWENTY-NINE) drugs to known pharmacogenomic phenotypes. Second, it leverages computable implementations of knowledge about pharmacogenomic phenotypes to compute drug selection or dosing recommendations based on computed phenotypes. For 3 drugs, recommendations can be generated both from the Clinical Pharmacogenomics Implementation Consortium (CPIC) guidelines in the United States and from the Dutch Pharmacogenomics Working Group (DPWG) guidelines developed in the Netherlands.

For genotype-to-phenotype mapping computations, the Services that come as part of the PGx-KA expect genotype input about an person encoded using diplotypes, like this: 

```JSON
{
    'CYP2D6':'*3/*3'
}
```

For phenotype-to-recommendation computations, inputs look like this:

```JSON
{
    'CYP2D6': {
        'diplotype': '*3/*3',
        'phenotype': 'Poor metabolizer'
    }
}
```

To try out the Knowlede Assembly and its functions, an interactive Google Colab workbook is available [online here](https://colab.research.google.com/drive/1giJbbABb2UBuFFSQPiIZBm7HVIc8-egI?usp=sharing).

- - - 

### Why was the PGx-KA example KA-KO initially created?

Expanding on its Purposes, the PGx-KA was initially created as an **experiement** in building Knowledge Assemblies by using and extending formal model for all Knowledge Objects, [KOIO 2.1] (https://github.com/kgrid/koio/releases/tag/2.1).

Several more specific goals met when initially creating the PGx-KA are these:

- The PGx-KA conforms to the KOIO 2.1 specification in all ways except when new terms were needed. The following new terms were developed or adopted from other sources in draft form as part of this work: Knowledge Assembly, KnowledgeSet, Purpose and hasKnowledgeObject.
- The PGx-KA uses more than one KnowledgeSet.
- The PGx-KA uses both KnowledgeSets defined in its metadata and a KnowledgeSet that is external to its metadata.
- The PGx-KA includes Services that make use of all of the KOs listed in each of its three KnowledgeSets. 

- - - 

### What does a diagram of the PGx-KA's components look like?

The PGx-KA can be depicted in a diagram showing its main components like this:

<img width="1239" height="761" alt="PGx-KA drawing v2" src="https://github.com/user-attachments/assets/c81f0160-9110-4bdb-b24b-ed4cd66e1c29" />

- - - 

### What metadata are provided with the PGx-KA?

The PGx-KA has its own [metadata file](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/metadata.json) with linked metadata in JSON.LD format that conform to KOIO 2.1. Information and links to all of the files included in the PGx-KA can be found in that metadata file.

- - -

### What Services does the PGx-KA include?

The PGx-KA includes three services:

- The Library Service enables application programmers to handle the KOs from PGx-KA as dependencies while treating the PGx-KA like any other JavaScript npm package.
- The API Service wraps the PGx-KA into an app that developers can use to engage the PGx-KA's content through a typical Restful API.
- The Plugin Service enables application programmers to manually load the KOs from the web while treating the PGx-KA like any other JavaScript npm package.

For more details about these three services, including technical instructions, see the [ServiceReadMe](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/ServiceReadMe.md) that comes with the PGx-KA.

- - - 

### What Tests does the PGx-KA include?

The PGx-KA includes two unit tests [here](https://github.com/kgrid-objects/pgx-knowledge-assembly/tree/main/pgx-ka/tests/unit).

The library-service.test.js file enables a PGx-KA user to test PGx-KA's Library service. The documentation for this test is [here](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/tests/library-service.readme.md).

The plugin-service.test.js file tests the PGx-KA's Plugin service. Its documentation is [here](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/tests/plugin-service.readme.md).

- - -

### What Documentation does the PGx-KA include?

The PGx-KA includes this ReadMe plus the following four other documentation artifacts:

- An Info Page automatically generated from the PGx-KA's own metadata file can be viewed online [here](https://kgrid-objects.github.io/pgx-knowledge-assembly/pgx_ka_info_page.html).
- Docs for describing PGx-KA's two Services are available [here](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/ServiceReadMe.md).
- Docs specifically for the Library Service unit test are [here](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/tests/library-service.readme.md).
- Docs specifically for the Plugin Service unit test are [here](https://github.com/kgrid-objects/pgx-knowledge-assembly/blob/main/pgx-ka/tests/plugin-service.readme.md).

- - - 

### What Other Resources for the PGx-KA are available?

- In this GitHub repository, there is an ipynb file for a Jupyter Notebook that has been made ready for use with VisualStudio Code.
- At this [link](https://colab.research.google.com/drive/1giJbbABb2UBuFFSQPiIZBm7HVIc8-egI?usp=sharing), there is a version of the Jupyter Notebook that uses the PGx-KA deployed as a Google Colab notebook. 

- - - 

### What sample Apps are available that make use of the PGx-KA?

Four sample apps that integrate the PGx-KA are available for inspection only. Just like the PGx-KA, these sample apps should **never be used to generate medical advice.** These  apps are  technical samples that exist **only** to show how knowledge assemblies can come with Services for app developers to use.

All four of these sample apps demonstrate how PGx-KA enables apps to compute phenotypes from genotypes first, and then to compute recommendations based on computed phenotypes.

The four sample apps can be found in this repo's [PGx-Demos folder](https://github.com/kgrid-objects/pgx-knowledge-assembly/tree/main/pgx-demos). What distinguishes these four sample apps is first the PGx-KA Service they use (Library vs. Plugin) and second whether the Knowledge from PGx-KA gets executed by a client or by a server. 

In addition, the first of these four sample apps - the pgx-demo-library-service-client-side-load app - is available for users to view online in a **test-only**, non-production deployment [here](https://kgrid-objects.github.io/pgx-knowledge-assembly/). 

The deployed sample app's user interface looks like this:

<img width="1415" height="1074" alt="image" src="https://github.com/user-attachments/assets/88231220-1ed6-4fea-b405-36a249bfd943" />

To see computed phenotypes and recommendations in the deployed sample app, click on any of the five simulated patients or enter diplotype information directly. **Never** use this sample app, or the other sample apps, or the PGx-KA to generate real medical advice. These items are only ever intended as technical demonstrations that illuminate how knowledge assemblies might be built and managed. 
 

