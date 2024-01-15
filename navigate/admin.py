from django.contrib import admin
from .models import Titles, BreakingNewsTitle , Tricker, StockReport, Logo, HeaderAddvertise, BrowserIcon, SocialLink, SinglePostTodayHeading, BreakingNewsWidget, DoNotMiss, AddvertiseWidget, Subscribe, SingleBlogPostContent, Marquee, EditorialPostSingleSlide,FooterHeadlinea,FooterHeadlineb,FooterHeadlinec,FooterHeadlined,FooterHeadlinee,FooterHeadlinef, FooterBgImg, FooterWidgetLista,FooterWidgetListb, FooterWidgetListc, FooterWidgetListd, FooterWidgetListe, FooterWidgetListf
from .models import CulturalNews, SportNews, SportNewsArea, CulturalNewsArea, GazetteCtaArea,SingleTeamArea,GazetteAboutUsArea,TeamArea, AboutUsBreadcumbArea, ContactAddressInfo, ContactUsBreadcumbArea, GazetteContactArea, CategoryBreadcumbArea, CatagoryGazetteWelcomePostAreaa, CatagoryGazetteWelcomePostAreab, CatagoryGazetteWelcomePostAreac, PaginationListItem, SinglePostArea, SinglePostAreaContents, SinglePostDiscussionArea, LeaveCommentArea, NavItem, NavItemDropDown, SearchArea
# Register your models here.
##Home Page / index.HTML Pages Models Are registered Here whic's are used as base.html..
admin.site.register(Titles)
admin.site.register(BrowserIcon)
admin.site.register(BreakingNewsTitle)
admin.site.register(Tricker)
admin.site.register(StockReport)
admin.site.register(Logo)


##Content's of Index.html Pages Models Are registered Here..
admin.site.register(HeaderAddvertise)
admin.site.register(SocialLink)
admin.site.register(SinglePostTodayHeading)

admin.site.register(BreakingNewsWidget)
admin.site.register(DoNotMiss)
admin.site.register(AddvertiseWidget)
admin.site.register(Subscribe)
admin.site.register(SingleBlogPostContent)
admin.site.register(Marquee)

admin.site.register(EditorialPostSingleSlide)

#Footer Content as Models Are Registered Here..
admin.site.register(FooterBgImg)
admin.site.register(FooterHeadlinea)
admin.site.register(FooterWidgetLista)

admin.site.register(FooterHeadlineb)
admin.site.register(FooterWidgetListb)

admin.site.register(FooterHeadlinec)
admin.site.register(FooterWidgetListc)

admin.site.register(FooterHeadlined)
admin.site.register(FooterWidgetListd)

admin.site.register(FooterHeadlinee)
admin.site.register(FooterWidgetListe)

admin.site.register(FooterHeadlinef)
admin.site.register(FooterWidgetListf)

# About Us Pages Models are Registered Here........
admin.site.register(AboutUsBreadcumbArea)
admin.site.register(GazetteAboutUsArea)
admin.site.register(TeamArea)
admin.site.register(SingleTeamArea)
admin.site.register(GazetteCtaArea)

#Contact Us pages Models Are Registered Here....
admin.site.register(ContactUsBreadcumbArea)
admin.site.register(GazetteContactArea)
admin.site.register(ContactAddressInfo)


#Category HTML Pages Models Are registered Here..
admin.site.register(CategoryBreadcumbArea)
admin.site.register(CatagoryGazetteWelcomePostAreaa)
admin.site.register(CatagoryGazetteWelcomePostAreab)
admin.site.register(CatagoryGazetteWelcomePostAreac)
admin.site.register(PaginationListItem)


#Single Post HTML Pages Models Are registered Here..
admin.site.register(SinglePostArea)
admin.site.register(SinglePostAreaContents)
admin.site.register(SinglePostDiscussionArea)
admin.site.register(LeaveCommentArea)

admin.site.register(SearchArea)

admin.site.register(CulturalNews)

admin.site.register(SportNews)

admin.site.register(CulturalNewsArea)

admin.site.register(SportNewsArea)