gene = "CYP2D6"


def diplotypes_for_phenotype(inputs):
    import csv
    import os

    output = {gene: {}}
    phenotype_value = inputs.get(gene)

    try:
        output[gene]["phenotype"] = phenotype_value
        output[gene]["diplotypes"] = []

        if phenotype_value is None:
            return output

        normalized_input = phenotype_value.strip().lower()
        if not normalized_input:
            return output

        csv_path = os.path.join(
            os.path.dirname(__file__), "CYP2D6_Diplotype_Phenotype_Table.csv"
        )
        try:
            with open(csv_path, newline="", encoding="utf-8-sig") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    raw_value = row["Coded Diplotype/Phenotype Summary"]
                    normalized_row_phenotype = (
                        "Unknown"
                        if raw_value is None
                        else raw_value.replace("CYP2D6 ", "").strip().capitalize()
                    ).lower()

                    if normalized_row_phenotype == normalized_input:
                        diplotype = row["CYP2D6 Diplotype"].strip()
                        if diplotype:
                            output[gene]["diplotypes"].append(diplotype)
        except Exception as csv_error:
            output[gene]["diplotypes"] = [f"CSV lookup error: {csv_error}"]

        return output
    except Exception as error:
        return f"Error {error}"
