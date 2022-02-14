import scrapy

class PersonalInfoSpider(scrapy.Spider):
    name = 'personal_info_itmo'
    start_urls = ['https://itmo.ru/ru/personlist/personalii.htm']

    def parse(self, response):
        for link in response.css('ul.nav.nav-pills.abcd a::attr(href)'):
            yield response.follow(link, callback=self.parse_page)

    def parse_page(self, response):
        for link in response.css('a.contact-pad::attr(href)'):
            yield response.follow(link, callback=self.parse_personal_info)

    def parse_personal_info(self, response):
        t_count_publication = response.xpath('//*[@href="#tabPublications"]/span//text()').get()
        ans_count_publication = 0
        if (t_count_publication != None):
            ans_count_publication = int(t_count_publication)
        return {
            'name': response.css('span.page-header-text::text').get(),
            'academic_degree': response.css('.c-personCard-details').xpath('dl[contains(./dt//text(),"Ученая степень:")]/dd/text()').get(),
            'count_post': len(response.css('.c-personCard-details').xpath('dl[contains(./dt//text(),"Должность:")]/dd/br')),
            'count_publication': ans_count_publication
        }