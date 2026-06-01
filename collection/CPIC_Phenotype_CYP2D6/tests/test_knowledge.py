import csv
import os

from cpic_phenotype_cyp2d6 import phenotype_by_diplotype
def test_phenotype_lookup(
    csv_path = os.path.join(os.path.dirname(__file__), "..", "cpic_phenotype_cyp2d6", "CYP2D6_Diplotype_Phenotype_Table.csv")
):
    """
    Ensure every unique phenotype output in the CSV
    can be generated.
    """

    expected_examples = {}

    with open(csv_path, mode="r", encoding="utf-8-sig") as file:

        reader = csv.reader(file)

        # Skip header row
        next(reader, None)

        for row in reader:

            if len(row) < 3:
                continue

            diplotype = row[0].strip()
            expected_output = row[2].replace("CYP2D6 ", "").strip().capitalize()

            if diplotype and expected_output:

                # Keep one representative example
                # for each distinct output
                expected_examples.setdefault(
                    expected_output,
                    diplotype
                )

    assert expected_examples, (
        "No valid phenotype outputs found."
    )

    print("\\nTesting phenotype outputs:\\n")

    for expected_output, diplotype in expected_examples.items():

        actual_output = phenotype_by_diplotype(
            {"CYP2D6": diplotype}
        )

        assert actual_output == {"CYP2D6": {"diplotype": diplotype, "phenotype": expected_output}}, (
            f"FAILED: {diplotype} -> "
            f"{actual_output} "
            f"(expected {expected_output})"
        )

        print(
            f"PASS: {diplotype} -> {actual_output}"
        )

    # Unknown lookup test
    assert phenotype_by_diplotype(
        {"CYP2D6": "not_a_real_diplotype"}
    ) == {"CYP2D6": {"diplotype": "not_a_real_diplotype", "phenotype": "Unknown"}}

    print("PASS: unknown diplotype -> unknown")

    # Blank input test
    assert phenotype_by_diplotype(
        {"CYP2D6": ""}
    ) == {"CYP2D6": {"diplotype": "", "phenotype": "Unknown"}}

    print("PASS: blank input -> unknown")

    # None input test
    assert phenotype_by_diplotype(
        {"CYP2D6": None}
    ) == {"CYP2D6": {"diplotype": None, "phenotype": "Unknown"}}

    print("PASS: None input -> unknown")

    print("\\nAll tests passed successfully.")
