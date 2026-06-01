gene = "CYP2D6"


def phenotype_by_diplotype(inputs):
    import csv
    import os
    output = {gene: {}}
    diplotype = inputs.get(gene)
    # Calculate using existing method
    try:
        
        output[gene]["diplotype"] = diplotype
        
        csv_path = os.path.join(os.path.dirname(__file__), "CYP2D6_Diplotype_Phenotype_Table.csv")
        try:
            with open(csv_path, newline="", encoding="utf-8-sig") as csvfile:
                reader = csv.DictReader(csvfile)
                output[gene]["phenotype"] = "Unknown"
                for row in reader:
                    if row["CYP2D6 Diplotype"].strip() == diplotype:
                        index = row["Coded Diplotype/Phenotype Summary"]
                        if index is None:
                            output[gene]["phenotype"] = "Unknown"
                        else:
                            output[gene]["phenotype"] = index.replace("CYP2D6 ", "").strip().capitalize()
                        
                        break
        except Exception as csv_error:
            output[gene]["phenotype"] = f"CSV lookup error: {csv_error}"
        return output
    except Exception as error:
        return f"Error {error}"
