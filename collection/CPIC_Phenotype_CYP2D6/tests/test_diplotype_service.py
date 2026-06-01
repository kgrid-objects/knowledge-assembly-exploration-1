from cpic_phenotype_cyp2d6 import diplotypes_for_phenotype


def test_reverse_service_for_IO_format_and_content():
    result = diplotypes_for_phenotype({"CYP2D6": "Poor metabolizer"})

    assert type(result) is dict
    assert result.keys() == {'CYP2D6'}
    assert result['CYP2D6'].keys() == {'phenotype', 'diplotypes'}
    assert result["CYP2D6"]["phenotype"] == "Poor metabolizer"
    assert "*3/*3" in result["CYP2D6"]["diplotypes"]


def test_reverse_service_unknown_phenotype_returns_empty_list():
    result = diplotypes_for_phenotype({"CYP2D6": "Not a real phenotype"})

    assert result == {
        "CYP2D6": {
            "phenotype": "Not a real phenotype",
            "diplotypes": [],
        }
    }
