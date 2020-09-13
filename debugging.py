 ##Set up URL to read with pandas
import pandas as pd
facts_url = 'https://space-facts.com/mars/'

    ##Read tabular data from page w/pandas
tables = pd.read_html(facts_url)

    ### Transpose table to make it usable
mars_facts = tables[0]
mars_facts_transposed = mars_facts.transpose()
    # print(mars_facts_transposed)

    ##Convert the data to an HTML table string
mars_facts_transposed_html = mars_facts_transposed.to_html()
print(mars_facts_transposed_html)