# Phenotype Service Specification 
This is a question-answering service for answering the following question, "What is the CYP2D6 phenotype associated with any given diploytype?"

This service accepts an input like

```
{
    'CYP2D6':'*3/*3'
}
```

 and it generates an output like

```
{
    'CYP2D6': {
        'diplotype': '*3/*3', 
        'phenotype': 'Poor metabolizer'
    }
}
```
