#CARD_READER SERVICE IS OFF
def test_input_units_REWORK(app):
    app.unit.find_units('REWORK')
    assert len(app.wd.find_elements_by_xpath("//div[@class='buttonPanel']/button[@disabled]"))
    assert len(app.wd.find_elements_by_xpath("//div[@id='e-sign' and text()='Check if card reader daemon is running']"))
    app.unit.submit_unit()