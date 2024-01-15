from django.shortcuts import render

# Create your views here.
from account.models import SubscribedUsers
from django.shortcuts import render
from postdetail.models import SinglePostToday, DetailPostHeading, TeamArea, SingleTeamArea
from video.models import NewsStream

from navigate.models import SportNewsArea, SportNews, HeaderAddvertise, BrowserIcon, SingleBlogPostContent, Logo, StockReport, Titles, Tricker, EditorialPostSingleSlide, FooterHeadlinea, FooterHeadlineb, FooterHeadlinec, FooterHeadlined, FooterHeadlinee, FooterHeadlinef, SinglePostDiscussionArea,LeaveCommentArea, FooterBgImg, FooterWidgetLista,FooterWidgetListb, FooterWidgetListc, FooterWidgetListd, FooterWidgetListe, FooterWidgetListf, Subscribe

from navigate.models import CulturalNews, CulturalNewsArea,Marquee, SinglePostTodayHeading, BreakingNewsWidget, DoNotMiss, AddvertiseWidget,  CatagoryGazetteWelcomePostAreaa, CatagoryGazetteWelcomePostAreab, CatagoryGazetteWelcomePostAreac, PaginationListItem, PaginationListNextButton,SearchArea

from navigate.models import BreakingNewsTitle,AboutUsBreadcumbArea,GazetteAboutUsArea,TeamArea,SingleTeamArea,SocialLink,  ContactUsBreadcumbArea, GazetteContactArea, ContactAddressInfo, CategoryBreadcumbArea, SinglePostArea, SinglePostAreaContents, GazetteCtaArea

# Create your views here.
def detailspost(request,id):

    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()
    
    #details = get_object_or_404(SignlePostToday, id=id)

    detailPostHeadings = DetailPostHeading.objects.all()

    postSingle = SinglePostToday.objects.get(pk=id)

    breakingnewswidgets = BreakingNewsWidget.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()
    
    return render(request,'detail.html',{'titles': titles, 'brknsts': brknsts, 
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'browser_icons': browser_icons,
                                    
                                    ## Header contents are passing by above's codes...............######.

                                    ## Block contents are passing by belows's codes...............................##########
                                    'detailPostHeadings' : detailPostHeadings,
                                    'postSingle': postSingle, 'breakingnewswidgets' : breakingnewswidgets,
                                    ## Block contents are passing by above's codes................####............####.......................

                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs
                                    #### Footer contents are passing by belows's codes...##############################............
                                    })


def breakingnewswidgetdetail(request, id):
    

    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()


    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)

    breakingnewswidgets = BreakingNewsWidget.objects.all()
    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request,          'breakingnewswidgetdetail.html', {'titles': titles, 'brknsts': brknsts, 
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets, 
    ## Footer contents are passing by belows's codes................##........##...................
        'ftrbgs':ftrbgs,
        'footerheadlineas': footerheadlineas,
        'footerheadlinebs': footerheadlinebs,
        'footerheadlinecs': footerheadlinecs, 
'footerheadlineds': footerheadlineds,
'footerheadlinees': footerheadlinees,
'footerheadlinefs': footerheadlinefs,
'footerwidgetlistas' : footerwidgetlistas,
'footerwidgetlistbs' : footerwidgetlistbs,
'footerwidgetlistcs' : footerwidgetlistcs,
'footerwidgetlistds' : footerwidgetlistds,
'footerwidgetlistes' : footerwidgetlistes,
'footerwidgetlistfs' : footerwidgetlistfs})

def newsstreamdetail(request,id):
    

    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()


    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    item =  NewsStream.objects.get(pk=id)

    sociallinks = SocialLink.objects.all()

    

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'newsstreamdetail.html', {'titles': titles, 'brknsts': brknsts, 
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'item' : item, 'sociallinks' : sociallinks,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets, 

                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs})



def gazettectaareadetail(request,id):

    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()

    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)

    gazettectaarea =  GazetteCtaArea.objects.get(pk=id)

    breakingnewswidgets = BreakingNewsWidget.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'gazettectaareadetail.html', {'titles': titles, 'brknsts': brknsts, 
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'gazettectaarea' : gazettectaarea,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets, 

                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs})




def aboutteamdetail(request,id):
    
    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()

    ###breakingnewswidgets = BreakingNewsWidget.objects.all()

    ###breakingnewswidget = BreakingNewsWidget.objects.get(pk=id)

    
    #teamarea = TeamArea.objects.get(pk=id)

    ##teamareas = TeamArea.objects.all(pk=id)

    singleteamarea = SingleTeamArea.objects.get(pk=id)

    
    
    sociallink = SocialLink.objects.all()

    postbreakingnewswidget = BreakingNewsWidget.objects.all()

    breakingnewswidgets = BreakingNewsWidget.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    
    
    ############################## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'aboutteamdetail.html', {'titles': titles, 'brknsts': brknsts,
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets,
                                     
                                    'singleteamarea' : singleteamarea,  'sociallink' : sociallink,
                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs})


def categorydetail(request,id):
    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()

    editorialpostsingleslide = EditorialPostSingleSlide.objects.get(pk=id)

    

    postbreakingnewswidget = BreakingNewsWidget.objects.all()

    breakingnewswidgets = BreakingNewsWidget.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    
    
    ############################## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()
    return render(request, "categorydetail.html", {'titles': titles, 'brknsts': brknsts,
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets,
                                    'editorialpostsingleslide' : editorialpostsingleslide, 
                                     
                                    
                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs})


def categorywelcomepostadetail(request,id):
    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()

    catagorygazettewelcomepostareaas = CatagoryGazetteWelcomePostAreaa.objects.all()

    catagorygazettewelcomepostareaa  = CatagoryGazetteWelcomePostAreaa.objects.get(pk=id)

    

    

    postbreakingnewswidget = BreakingNewsWidget.objects.all()

    breakingnewswidgets = BreakingNewsWidget.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    
    
    ############################## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()
    
    return render(request, "categorywelcomepostadetail.html", {'titles': titles, 'brknsts': brknsts,
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets,
                                    'catagorygazettewelcomepostareaa' : catagorygazettewelcomepostareaa, 
                                     'catagorygazettewelcomepostareaas' : catagorygazettewelcomepostareaas,
                                    
                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs})


def categorywelcomepostbdetail(request,id):
    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()

    
    catagorygazettewelcomepostareabs = CatagoryGazetteWelcomePostAreab.objects.all()
    catagorygazettewelcomepostareab = CatagoryGazetteWelcomePostAreab.objects.get(pk=id)

    

    

    postbreakingnewswidget = BreakingNewsWidget.objects.all()

    breakingnewswidgets = BreakingNewsWidget.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    
    
    ############################## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()
    
    return render(request, "categorywelcomepostbdetail.html", {'titles': titles, 'brknsts': brknsts,
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets,
                                    'catagorygazettewelcomepostareab' : catagorygazettewelcomepostareab,  'catagorygazettewelcomepostareabs' :catagorygazettewelcomepostareabs,
                                    
                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs})


def categorywelcomepostcdetail(request,id):
    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()

    
    catagorygazettewelcomepostareacs = CatagoryGazetteWelcomePostAreac.objects.all()
    catagorygazettewelcomepostareac = CatagoryGazetteWelcomePostAreac.objects.get(pk=id)

    

    

    postbreakingnewswidget = BreakingNewsWidget.objects.all()

    breakingnewswidgets = BreakingNewsWidget.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    
    
    ############################## First Column Is here
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()
    
    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()
    
    return render(request, "categorywelcomepostcdetail.html", {'titles': titles, 'brknsts': brknsts,
                                    'news_trickers': news_trickers, 'stock_reports' : stock_reports,
                                    'site_logos': site_logos, 'header_adds': header_adds,
                                    'browser_icons': browser_icons, 'postbreakingnewswidget' : postbreakingnewswidget, 'breakingnewswidgets' : breakingnewswidgets,
                                    'catagorygazettewelcomepostareac' : catagorygazettewelcomepostareac,  'catagorygazettewelcomepostareacs' :catagorygazettewelcomepostareacs,
                                    
                                    ## Footer contents are passing by belows's codes................##........##...................
                                    'ftrbgs':ftrbgs,
                                    'footerheadlineas': footerheadlineas,
                                    'footerheadlinebs': footerheadlinebs,
                                    'footerheadlinecs': footerheadlinecs, 
                                    'footerheadlineds': footerheadlineds,
                                    'footerheadlinees': footerheadlinees,
                                    'footerheadlinefs': footerheadlinefs,
                                    'footerwidgetlistas' : footerwidgetlistas,
                                    'footerwidgetlistbs' : footerwidgetlistbs,
                                    'footerwidgetlistcs' : footerwidgetlistcs,
                                    'footerwidgetlistds' : footerwidgetlistds,
                                    'footerwidgetlistes' : footerwidgetlistes,
                                    'footerwidgetlistfs' : footerwidgetlistfs})



def sportnewsdetailtop(request, id):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    
    #Single Post . HTML Codes Are Here....
    sportnewsareas = SportNewsArea.objects.all()
    sportnewsarea = SportNewsArea.objects.get(pk=id)
    

    sportnewss = SportNews.objects.all()

    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    

    #Single Post Discussion Area
    
    
    ##commentpersons = CommentPerson.objects.all()

    #Comment Leave Form
    leavecommentareas = LeaveCommentArea.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()

    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'sportnewsdetailtop.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'sportnewss': sportnewss, 'sportnewsarea': sportnewsarea, 'sportnewsareas' : sportnewsareas,
    'postbreakingnewswidget' : postbreakingnewswidget,  'breakingnewswidgets' : breakingnewswidgets,
    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })




def sportnewsdetailmid(request, id):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    
    #Single Post . HTML Codes Are Here....
    
    
    sportnewss = SportNews.objects.all()
    sportnews = SportNews.objects.get(pk=id)
    

    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    

    #Single Post Discussion Area
    
    
    ##commentpersons = CommentPerson.objects.all()

    #Comment Leave Form
    leavecommentareas = LeaveCommentArea.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()

    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'sportnewsdetailmid.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'sportnewss': sportnewss,  'sportnews' :sportnews,
    'postbreakingnewswidget' : postbreakingnewswidget,  'breakingnewswidgets' : breakingnewswidgets,
    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
})



def culturalnewsdetailtop(request, id):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    
    #Single Post . HTML Codes Are Here....
    culturalnewsareas = CulturalNewsArea.objects.all()
    culturalnewsarea = CulturalNewsArea.objects.get(pk=id)

    

    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    

    #Single Post Discussion Area
    
    
    ##commentpersons = CommentPerson.objects.all()

    #Comment Leave Form
    leavecommentareas = LeaveCommentArea.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()

    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'culturalnewsdetailtop.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'culturalnewsareas' : culturalnewsareas, 'culturalnewsarea' : culturalnewsarea,
    'postbreakingnewswidget' : postbreakingnewswidget,  'breakingnewswidgets' : breakingnewswidgets,
    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })




def culturalnewsdetailmid(request, id):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    
    #Single Post . HTML Codes Are Here....
    culturalnewss = CulturalNews.objects.all()
    culturalnews = CulturalNews.objects.get(pk=id)

    

    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    

    #Single Post Discussion Area
    
    
    ##commentpersons = CommentPerson.objects.all()

    #Comment Leave Form
    leavecommentareas = LeaveCommentArea.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()

    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'culturalnewsdetailmid.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'culturalnews' : culturalnews, 'culturalnewss' : culturalnewss,
    'postbreakingnewswidget' : postbreakingnewswidget,  'breakingnewswidgets' : breakingnewswidgets,
    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })


def singlepostdetailtop(request, id):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    
    #Single Post . HTML Codes Are Here....
    singlepostareas = SinglePostArea.objects.all()
    singlepostarea = SinglePostArea.objects.get(pk=id)

    

    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    

    #Single Post Discussion Area
    
    
    ##commentpersons = CommentPerson.objects.all()

    #Comment Leave Form
    leavecommentareas = LeaveCommentArea.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()

    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'singlepostdetailtop.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'singlepostarea' : singlepostarea, 'singlepostareas' : singlepostareas,  
    'postbreakingnewswidget' : postbreakingnewswidget,  'breakingnewswidgets' : breakingnewswidgets,
    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })


def singlepostdetailmid(request, id):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    
    #Single Post . HTML Codes Are Here....
    

    singlepostareacontents = SinglePostAreaContents.objects.all()
    singlepostareacontent = SinglePostAreaContents.objects.get(pk=id)

    postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    

    #Single Post Discussion Area
    
    
    ##commentpersons = CommentPerson.objects.all()

    #Comment Leave Form
    leavecommentareas = LeaveCommentArea.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()

    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'singlepostdetailmid.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    'singlepostareacontents' : singlepostareacontents, 'singlepostareacontent' : singlepostareacontent, 

    #Single Post . Html Codes Are here

    
    'postbreakingnewswidget' : postbreakingnewswidget,  'breakingnewswidgets' : breakingnewswidgets,
    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })





def singleblogpostcontentdetailtop(request, id):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    
    #Single Post . HTML Codes Are Here....
    
    singlebBlogPostContents = SingleBlogPostContent.objects.all()
    singlebBlogPostContent = SingleBlogPostContent.objects.get(pk=id)
    

    #postbreakingnewswidget = BreakingNewsWidget.objects.get(pk=id)
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    

    #Single Post Discussion Area
    
    
    ##commentpersons = CommentPerson.objects.all()

    #Comment Leave Form
    leavecommentareas = LeaveCommentArea.objects.all()

    ftrbgs = FooterBgImg.objects.all()
    ## First Column Is here
    
    footerheadlineas = FooterHeadlinea.objects.all()

    footerwidgetlistas = FooterWidgetLista.objects.all()

    footerheadlinebs = FooterHeadlineb.objects.all()

    footerwidgetlistbs = FooterWidgetListb.objects.all()

    footerheadlinecs = FooterHeadlinec.objects.all()

    footerwidgetlistcs = FooterWidgetListc.objects.all()

    footerheadlineds = FooterHeadlined.objects.all()

    footerwidgetlistds = FooterWidgetListd.objects.all()

    footerheadlinees = FooterHeadlinee.objects.all()

    footerwidgetlistes = FooterWidgetListe.objects.all()

    footerheadlinefs = FooterHeadlinef.objects.all()

    footerwidgetlistfs = FooterWidgetListf.objects.all()

    return render(request, 'singleblogpostcontentdetailtop.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'singlebBlogPostContents' : singlebBlogPostContents, 'singlebBlogPostContent' : singlebBlogPostContent,
    'breakingnewswidgets' : breakingnewswidgets,
    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })
