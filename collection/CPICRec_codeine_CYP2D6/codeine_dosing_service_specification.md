# Codeine Dosing Service Specification 
This is a question-answering service for answering the following question, "What is the CYP2D6 phenotype associated with any given diploytype?"

This service accepts an input like

```
{
    'CYP2D6': {
        'phenotype': 'Poor metabolizer'
    }
}
```

 and it generates an output like

```
{   
    'type': 'CPIC Recommendation',
    'drug': 'Codeine',
    'genes': {
        'CYP2D6': {
            'diplotype': '', 
            'phenotype': 'poor metabolizer'
        }
    },
    'recommendation': {
        'implication': 'Greatly reduced morphine formation following codeine administration, leading to insufficient pain relief.',
        'content': 'Avoid codeine use due to lack of efficacy. Alternatives that are not affected by this CYP2D6 phenotype include morphine and nonopioid analgesics. Tramadol and, to a lesser extent, hydrocodone and oxycodone are not good alternatives because their metabolism is affected by CYP2D6 activity; these agents should be avoided',
        'classification': 'Strong'
    }
}
```
