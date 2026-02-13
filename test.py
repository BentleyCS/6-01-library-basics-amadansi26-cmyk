import CSP_6_01_Library_Basics as HW

def test_process_expenses():
    assert HW.process_expenses([100,20])==[115.0, 23.0]


def test_analyze_scores():
    assert HW.analyze_scores([100,50,75]) ==[100, 75.0]


def test_sanitize_usernames():
    assert HW.sanitize_usernames("John Mack" "Albert K")


def test_identify_outliers():
    assert HW.identify_outliers([101, 90, 200]) == [100, 200]


def test_search_and_report():
    assert HW.search_and_report(["  Apple", "Banana ", "  CHERRY  "], "banana") == 1
    assert HW.search_and_report(["  Apple", "Banana ", "  CHERRY  "], "pineapple") == -1
