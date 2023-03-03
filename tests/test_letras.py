def test_remover_acento():
    var_l = "delírio"
    assert var_l.replace("í","i") == "delirio"