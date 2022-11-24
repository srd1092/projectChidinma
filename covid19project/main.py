import methods


if __name__ == '__main__':
    methods.filter_with_iso_code("owid-covid-data-europe-all.csv", "new_cases", "ALB")
    # methods.min_max("owid-covid-data-europe-all.csv", "new_cases")
    # methods.average_value("owid-covid-data-europe-all.csv", "total_cases")
    # methods.generate_bar_graph("owid-covid-data-europe-all.csv", "total_cases")
