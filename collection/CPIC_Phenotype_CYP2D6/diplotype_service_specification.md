# Diplotype for Phenotype Service Specification
This is a question-answering service for answering the following question, "What are the diplotypes associated with any given CYP2D6 phenotype?"

This service accepts an input like

```
{
    'CYP2D6': 'Poor metabolizer'
}
```

and it generates an output like

```
{
    'CYP2D6': {
        'phenotype': 'Poor metabolizer',
        'diplotypes': ['*3/*3', '*3/*4', '...']
    }
}
```
