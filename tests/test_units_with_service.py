#CARD_READER SERVICE IS ON
def test_input_units_REWORK(app):
    app.unit.find_units('REWORK')
    assert len(app.wd.find_elements_by_xpath("//div[@class='buttonPanel']/button[@id='ok_button']"))
    assert len(app.wd.find_elements_by_xpath("//div[@id='e-sign' and text()='Full name:   Vladyslav   Velychko']"))

def test_input_units_CONTINUE(app):
    app.unit.find_units('CONTINUE')
    assert len(app.wd.find_elements_by_xpath("//div[@class='buttonPanel']/button[@id='ok_button']"))
    assert len(app.wd.find_elements_by_xpath("//div[@id='e-sign' and text()='Full name:   Vladyslav   Velychko']"))

