import copy
drug = "codeine"
reference = {"CYP2D6": {"field": "phenotype", "value": ""}}
keysuffix = {"CYP2D6": {"positive": "", "negative": ""}}  # adjust if needed
recommendations = {
    "cyp2d6ultrarapid": {
        "implication": "Increased formation of morphine following codeine administration, leading to higher risk of toxicity",
        "recommendation": "Avoid codeine use due to potential for toxicity. Alternatives that are not affected by this CYP2D6 phenotype include morphine and nonopioid analgesics. Tramadol and, to a lesser extent, hydrocodone and oxycodone are not good alternatives because their metabolism is affected by CYP2D6 activity",
        "classification": "Strong",
    },
    "cyp2d6normal": {
        "implication": "Normal morphine formation",
        "recommendation": "Use label-recommended age- or weight-specific dosing.",
        "classification": "Strong",
    },
    "cyp2d6intermediate": {
        "implication": "Reduced morphine formation",
        "recommendation": "Use label-recommended age- or weight-specific dosing. If no response, consider alternative analgesics such as morphine or a nonopioid. Monitor tramadol use for response.",
        "classification": "Moderate",
    },
    "cyp2d6poor": {
        "implication": "Greatly reduced morphine formation following codeine administration, leading to insufficient pain relief.",
        "recommendation": "Avoid codeine use due to lack of efficacy. Alternatives that are not affected by this CYP2D6 phenotype include morphine and nonopioid analgesics. Tramadol and, to a lesser extent, hydrocodone and oxycodone are not good alternatives because their metabolism is affected by CYP2D6 activity; these agents should be avoided",
        "classification": "Strong",
    },
}


def dosingrecommendation(inputs):
    """
    Receives phenotype and returns the recommendation.

    Parameters:
    ----------
    inputs : dict
        A dictionary containing gene information, where keys are gene names (EX {'CYP2D6': {'phenotype': 'Normal metabolizer'}})
    

    Returns:
    -------
        Codeine recommendation based on phenotype.
    
    """
    try:
        genes = {}
        output = {}
        searchkey_ready = True
        lowercase_input = {}
        search_key = ""

        # convert input keys to lowercase
        for inputkey, value in inputs.items():
            lowercase_input[inputkey.lower()] = value

        for genekey, ref in reference.items():
            key = genekey.lower()
            if key not in lowercase_input:
                break

            genes[genekey] = {}
            genes[genekey]["diplotype"] = lowercase_input[key].get("diplotype", "")
            genes[genekey]["phenotype"] = lowercase_input[key].get("phenotype", "").lower()

            targetfield = ref["field"]
            searchkey_ready = searchkey_ready and genes[genekey].get(targetfield, "") != ""

            if targetfield == "diplotype":
                if ref["value"] in genes[genekey]["diplotype"]:
                    search_key += key + ref["value"] + keysuffix[genekey]["positive"]
                else:
                    search_key += key + ref["value"] + keysuffix[genekey]["negative"]

            if targetfield == "phenotype":
                if genes[genekey]["phenotype"] != "":
                    pheno = genes[genekey]["phenotype"].replace("metabolizer", "").replace(" ", "")
                    search_key += key + pheno

        if searchkey_ready:
            if search_key in recommendations:
                output["type"] = "CPIC Recommendation"
                output["drug"] = drug
                output["genes"] = copy.deepcopy(genes)
                rec = recommendations[search_key]
                output["recommendation"] = {
                    "implication": rec["implication"],
                    "content": rec["recommendation"],
                    "classification": rec["classification"],
                }
                return output
            else:
                return f"Incorrect/invalid input for drug {drug}"
        else:
            return "Incorrect/invalid input."

    except Exception as error:
        return f"Error: {error}"

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

def main():
    try:
        import argparse

        parser = argparse.ArgumentParser(description="Codeine avoidance check based on diplotype")
        parser.add_argument('--diplotype', type=str, default=None, help="The individual's diplotype for CYP2D6 (e.g., *7/*8)")
        args = parser.parse_args()

        if not args.diplotype:
            print("Find out whether someone should AVOID codeine.")
            diplotype = input("Enter an individual's diplotype for CYP2D6 (EX *7/*8): ")
        else:
            diplotype = args.diplotype
        recommendation = dosingrecommendation(phenotype_by_diplotype({"CYP2D6": diplotype}))

        print("****************Answer**********************")
        if "avoid" in recommendation["recommendation"]["content"].lower():
            print("AVOID codeine.")
        else:
            print("Codeine OK.")
        print(f"Why? This person is a '{recommendation['genes']['CYP2D6']['phenotype']}'.")    
        print("********************************************")
    except Exception as e:
        print(f"App was stopped. Error: {e}")
if __name__ == "__main__":
    main()


