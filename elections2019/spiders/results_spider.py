import scrapy
from scrapy import Request

class CWACResultsSpider(scrapy.Spider):
    name = "cw-all-candidates"

    def start_requests(self):
        # Andhra Pradesh
        for i in range(175):
            yield Request('https://results.eci.gov.in/ac/en/constituencywise/ConstituencywiseS01%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Odisha
        for i in range(146):
            yield Request('https://results.eci.gov.in/ac/en/constituencywise/ConstituencywiseS18%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Arunachal Pradesh
        for i in range(60):
            yield Request('https://results.eci.gov.in/ac/en/constituencywise/ConstituencywiseS02%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Sikkim
        for i in range(32):
            yield Request('https://results.eci.gov.in/ac/en/constituencywise/ConstituencywiseS21%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

    def parse(self, response):
        results = response.css('#div1 > table > tbody > tr')
        for result in results[3:len(results)-1]:
            yield {
                'State': results[0].css('td::text').extract_first().split('-')[0].strip(),
                'Constituency': results[0].css('td::text').extract_first().split('-')[1].strip(),
                'O.S.N.': result.css('td::text')[0].extract(),
                'Candidate': result.css('td::text')[1].extract(),
                'Party': result.css('td::text')[2].extract(),
                'EVM Votes': result.css('td::text')[3].extract(),
                'Postal Votes': result.css('td::text')[4].extract(),
                'Total Votes': result.css('td::text')[5].extract(),
                'Pct of Votes': result.css('td::text')[6].extract(),
            }

class CWLSResultsSpider(scrapy.Spider):
    name = "cw-all-candidates-ls"

    def start_requests(self):
        # Andaman & Nicobar Islands
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU01%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Andhra Pradesh
        for i in range(25):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS01%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Arunachal Pradesh
        for i in range(2):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS02%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Assam
        for i in range(14):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS03%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Bihar
        for i in range(40):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS04%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Chandigarh
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU02%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Chhattisgarh
        for i in range(11):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS26%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Dadra & Nagar Haveli
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU03%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Delhi
        for i in range(7):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU05%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Daman & Diu
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU04%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Goa
        for i in range(2):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS05%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Gujarat
        for i in range(26):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS06%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Haryana
        for i in range(10):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS07%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Himachal Pradesh
        for i in range(4):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS08%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Jammu & Kashmir
        for i in range(6):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS09%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Jharkhand
        for i in range(14):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS27%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Karnataka
        for i in range(28):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS10%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Kerala
        for i in range(20):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS11%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Lakshadweep
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU06%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Madhya Pradesh
        for i in range(29):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS12%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Maharashtra
        for i in range(48):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS13%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Manipur
        for i in range(2):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS14%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Meghalaya
        for i in range(2):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS15%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Mizoram
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS16%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Nagaland
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS17%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Odisha
        for i in range(21):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS18%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Puducherry
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU07%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Punjab
        for i in range(13):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS19%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Rajasthan
        for i in range(25):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS20%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Sikkim
        for i in range(1):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS21%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Tamil Nadu
        for i in range(39):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS22%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Telangana
        for i in range(17):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS29%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Tripura
        for i in range(2):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS23%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Uttar Pradesh
        for i in range(80):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS24%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # Uttarakhand
        for i in range(5):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS28%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)

        # West Bengal
        for i in range(42):
            yield Request('https://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS25%s.htm?ac=%s' % (i+1,i+1), callback=self.parse)



    def parse(self, response):
        results = response.css('#div1 > table > tbody > tr')
        for result in results[3:len(results)-1]:
            yield {
                'State': results[0].css('th::text').extract_first().split('-')[0].strip(),
                'Constituency': results[0].css('th::text').extract_first().split('-')[1].strip(),
                'O.S.N.': result.css('td::text')[0].extract(),
                'Candidate': result.css('td::text')[1].extract(),
                'Party': result.css('td::text')[2].extract(),
                'EVM Votes': result.css('td::text')[3].extract(),
                'Postal Votes': result.css('td::text')[4].extract(),
                'Total Votes': result.css('td::text')[5].extract(),
                'Pct of Votes': result.css('td::text')[6].extract(),
            }

