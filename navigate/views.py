from ast import Param
from django.conf import settings
#from contextlib import _RedirectStream
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import date, datetime
from django.views.decorators.csrf import csrf_exempt
from time import time
from django.shortcuts import render
from django.db.models import Q
from account.models import SubscribedUsers
from .forms import NewsletterForm
from video.models import NewsStream
from pyexpat.errors import messages
from email.message import EmailMessage
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, auth

from navigate.models import HeaderAddvertise, BrowserIcon, SingleBlogPostContent, Logo, StockReport, Titles, Tricker, EditorialPostSingleSlide, FooterHeadlinea, FooterHeadlineb, FooterHeadlinec, FooterHeadlined, FooterHeadlinee, FooterHeadlinef, SinglePostDiscussionArea,LeaveCommentArea, FooterBgImg, FooterWidgetLista,FooterWidgetListb, FooterWidgetListc, FooterWidgetListd, FooterWidgetListe, FooterWidgetListf, Subscribe

from navigate.models import Marquee, SinglePostTodayHeading, BreakingNewsWidget, DoNotMiss, AddvertiseWidget, CatagoryGazetteWelcomePostAreaa, CatagoryGazetteWelcomePostAreab, CatagoryGazetteWelcomePostAreac, PaginationListItem, PaginationListNextButton,SearchArea

from navigate.models import SportNews, SportNewsArea, CulturalNews, CulturalNewsArea, GazetteCtaArea, BreakingNewsTitle,AboutUsBreadcumbArea,GazetteAboutUsArea,TeamArea,SingleTeamArea,SocialLink, ContactUsBreadcumbArea, GazetteContactArea, ContactAddressInfo, CategoryBreadcumbArea, SinglePostArea, SinglePostAreaContents
from postdetail.models import SinglePostToday
from account.models import CommentPerson
# Create your views here.
def index(request):

    titles = Titles.objects.all()
    browser_icons = BrowserIcon.objects.all()
    brknsts = BreakingNewsTitle.objects.all()
    #Changing News tricker Below the Breaking News Title
    
    news_trickers = Tricker.objects.all()
    #Changing Stock Report Below the Breaking News Title


    stock_reports = StockReport.objects.all()
    site_logos = Logo.objects.all()
    header_adds = HeaderAddvertise.objects.all()


    #Social Links
    
    newsstream = NewsStream.objects.all()
    sociallinks = SocialLink.objects.all()


    #Only for Single-post Heading
    singleposttodayheadings = SinglePostTodayHeading.objects.all()
    
    
    postSingles = SinglePostToday.objects.all()

    
    breakingnewswidgets = BreakingNewsWidget.objects.all()
    
    donotmisss = DoNotMiss.objects.all()

    addvertisewidgets = AddvertiseWidget.objects.all()
    

    subscribeforms = Subscribe.objects.all()
    

    #Single Blog Post Slider Contents Start From Here
    singlebBlogPostContents = SingleBlogPostContent.objects.all()
    
    marquees = Marquee.objects.all()
    
    #Single Video Post Content
    
    
    editorialpostsingleslides = EditorialPostSingleSlide.objects.all()
    

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

    return render(request, 'index.html', {'titles': titles, 'brknsts': brknsts,
    
    'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds,

    'browser_icons': browser_icons,

    'newsstream' : newsstream,

    'sociallinks' : sociallinks,

    'singlebBlogPostContents': singlebBlogPostContents,

    'marquees' : marquees,
    
    'singleposttodayheadings' : singleposttodayheadings,

    'postSingles' :  postSingles,

    'breakingnewswidgets' : breakingnewswidgets,

    'donotmisss' : donotmisss, 'addvertisewidgets' : addvertisewidgets,
    
    'subscribeforms' : subscribeforms,
    
    'editorialpostsingleslides' : editorialpostsingleslides,
    
    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    
    
    })



def about(request):

    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    

    news_trickers = Tricker.objects.all()
    
    
    #Changing Stock Report Below the Breaking News Title


    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()

    
    #Changing Stock Report Below the Breaking News Title 
    

    
    #About-Us page's Classes objects are called from here
    aboutusbreadcumbareas =  AboutUsBreadcumbArea.objects.all()
    

    #Gazette about us area text content
    gazetteaboutusareas = GazetteAboutUsArea.objects.all()
    


    #Team area contents including team heading
    teamareas = TeamArea.objects.all()

    #Single Team Area Including Images and Heading
    singleteamareas = SingleTeamArea.objects.all()
    
    #Social Links
    sociallinks = SocialLink.objects.all()

    #Gazette Cta Area Objects and Clases Codes are given below....
    
    gazettectaareas = GazetteCtaArea.objects.all()
    

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

    return render(request, 'about-us.html', {'titles': titles, 
    
    'news_trickers': news_trickers, 'brknsts' : brknsts, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,

    

    #passing about us pages objects..
    'aboutusbreadcumbareas' : aboutusbreadcumbareas, 'gazetteaboutusareas' : gazetteaboutusareas, 'teamareas' : teamareas,

    'singleteamareas' : singleteamareas,    'sociallinks' : sociallinks,   'gazettectaareas' : gazettectaareas,

    'ftrbgs' : ftrbgs,  

    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    
    })


def contact(request):

    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()
 
    

    #Contact Us Breadcumb Area Start

    contactusbreadcumbareas =  ContactUsBreadcumbArea.objects.all()
    
    #Contact Us Breadcumb Area End
    gazettecontactareas = GazetteContactArea.objects.all()
    
    #Contact Address Info Part Here
    contactaddressinfos = ContactAddressInfo.objects.all()
    
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

    return render(request, 'contact.html', {'titles': titles, 
    
    'news_trickers': news_trickers, 'stock_reports' : stock_reports, 'brknsts' : brknsts,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    


    'contactusbreadcumbareas' : contactusbreadcumbareas,

    'gazettecontactareas' : gazettecontactareas,

    'contactaddressinfos' : contactaddressinfos,

    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    
    })
#Category Pages Method Starts From Here
def category(request):

    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()
    

    #CategoryBreadcumbArea
    categorybreadcumbareas = CategoryBreadcumbArea.objects.all()
    
    editorialpostsingleslides = EditorialPostSingleSlide.objects.all()

    # Catagory Gazette Welcome Post Area.......
    catagorygazettewelcomepostareaas = CatagoryGazetteWelcomePostAreaa.objects.all()

    catagorygazettewelcomepostareabs = CatagoryGazetteWelcomePostAreab.objects.all()

    catagorygazettewelcomepostareacs = CatagoryGazetteWelcomePostAreac.objects.all()
    
    
    
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
    
    return render(request, 'category.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds,

    'browser_icons': browser_icons,
    

    'categorybreadcumbareas' : categorybreadcumbareas, 'editorialpostsingleslides': editorialpostsingleslides,
    
    'catagorygazettewelcomepostareaas' : catagorygazettewelcomepostareaas, 'catagorygazettewelcomepostareabs' : catagorygazettewelcomepostareabs,
    
    'catagorygazettewelcomepostareacs' : catagorygazettewelcomepostareacs,

    
    
    
    'editorialpostsingleslides' : editorialpostsingleslides, 'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    })

def singlepost(request):
    
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
    

    singlepostareacontents = SinglePostAreaContents.objects.all()

    #Single Post Discussion Area
    singlepostdiscussionareas = SinglePostDiscussionArea.objects.all()
    
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

    return render(request, 'single-post.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'singlepostareas' : singlepostareas, 'singlepostdiscussionareas' : singlepostdiscussionareas,

    'singlepostareacontents' : singlepostareacontents,

    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })

#Search Function Starts from Here
def search(request):
    
    titles = Titles.objects.all()

    browser_icons = BrowserIcon.objects.all()
    
    brknsts = BreakingNewsTitle.objects.all()
    

    #Changing News tricker Below the Breaking News Title
    news_trickers = Tricker.objects.all()
    
    #Changing Stock Report Below the Breaking News Title
    stock_reports = StockReport.objects.all()
    
    site_logos = Logo.objects.all()

    header_adds = HeaderAddvertise.objects.all()



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
    
    if request.method == 'GET':
        query = request.GET.get("query")
        if query:
            searchareas = SearchArea.objects.filter(searchpostheadline__icontains=query)
           
            singlepostareas = SinglePostArea.objects.filter(tag__icontains=query)
            
            singlepostareacontents = SinglePostAreaContents.objects.filter(blockqts__icontains=query)

            leavecommentareas = LeaveCommentArea.objects.filter(formbtn__icontains=query)

            singleposttodays = SinglePostToday.objects.filter(tag__icontains=query)

            singleteamareas = SingleTeamArea.objects.filter(name__icontains=query)

            catagorygazettewelcomepostareaas = CatagoryGazetteWelcomePostAreaa.objects.filter(gazetteposttag__icontains=query)

            catagorygazettewelcomepostareabs = CatagoryGazetteWelcomePostAreab.objects.filter(gazetteposttag__icontains=query)

            catagorygazettewelcomepostareacs = CatagoryGazetteWelcomePostAreac.objects.filter(gazetteposttag__icontains=query)
            
            

            breakingnewswidgets = BreakingNewsWidget.objects.filter(widget_title__icontains=query)
            
            return render(request, 'search.html', {'singleteamareas': singleteamareas, 'searchareas': searchareas, 'singlepostareas' : singlepostareas, 
            
            'singlepostareacontents': singlepostareacontents, 'leavecommentareas' : leavecommentareas, 

            'singleposttodays': singleposttodays, 
            
            'catagorygazettewelcomepostareaas' :catagorygazettewelcomepostareaas,
            'catagorygazettewelcomepostareabs': catagorygazettewelcomepostareabs, 
            'catagorygazettewelcomepostareacs' : catagorygazettewelcomepostareacs,

            
            'breakingnewswidgets' : breakingnewswidgets,

            'titles':titles, 'brknsts': brknsts,  'news_trickers': news_trickers, 'stock_reports' : stock_reports,
            'site_logos': site_logos,   'header_adds': header_adds,'browser_icons': browser_icons,
            
            
            'ftrbgs' : ftrbgs,
            'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
            'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
            'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
            'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
            'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
            'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs})
             
        
            
                    
        else:
            messages.success(request, "Nothing matched with your search!")
            redirect('/')
            return render(request, 'search.html', {'titles':titles, 'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,'site_logos': site_logos, 'header_adds': header_adds,'browser_icons': browser_icons,
            
            
            'ftrbgs' : ftrbgs,
            'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
            'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
            'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
            'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
            'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
            'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs})



def culturalnews(request):
    
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
    

    culturalnewsareas = CulturalNewsArea.objects.all()
    
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

    return render(request, 'culturalnews.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'culturalnewsareas' : culturalnewsareas, 'culturalnewss' : culturalnewss, 

    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })


def sportnews(request):
    
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
    

    sportnewss = SportNews.objects.all()

    

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

    return render(request, 'sportnews.html', {'titles':titles,
    
    'brknsts': brknsts, 'news_trickers': news_trickers, 'stock_reports' : stock_reports,

    'site_logos': site_logos, 'header_adds': header_adds, 'browser_icons': browser_icons,
    
    

    #Single Post . Html Codes Are here

    'sportnewss': sportnewss, 'sportnewsareas': sportnewsareas,

    

    'leavecommentareas' : leavecommentareas,    'ftrbgs' : ftrbgs,
    
    'footerheadlineas' : footerheadlineas,  'footerwidgetlistas' :footerwidgetlistas, 
    'footerheadlinebs' : footerheadlinebs,  'footerwidgetlistbs' :footerwidgetlistbs, 
    'footerheadlinecs' : footerheadlinecs,  'footerwidgetlistcs' :footerwidgetlistcs,
    'footerheadlineds' : footerheadlineds,  'footerwidgetlistds' :footerwidgetlistds,  
    'footerheadlinees' : footerheadlinees,  'footerwidgetlistes' :footerwidgetlistes, 
    'footerheadlinefs' : footerheadlinefs,  'footerwidgetlistfs' :footerwidgetlistfs,
    

    #Single Post . Html Codes Are here
    
    })


