
from itertools import permutations
from extensions.enigma import Enigma
from analysis import brute

if __name__ == '__main__':
    
    # E = Enigma(0, [0, 3, 2], [8, 4, 19], [1, 14, 21], 'AF-TN-KO-BL-RW')
    # p = 'IPROPOSETOCONSIDERTHEQUESTIONCANMACHINESTHINKTHISSHOULDBEGINWITHDEFINITIONSOFTHEMEANINGOFTHETERMSMACHINEANDTHINKTHEDEFINITIONSMIGHTBEFRAMEDSOASTOREFLECTSOFARASPOSSIBLETHENORMALUSEOFTHEWORDSBUTTHISATTITUDEISDANGEROUSIFTHEMEANINGOFTHEWORDSMACHINEANDTHINKARETOBEFOUNDBYEXAMININGHOWTHEYARECOMMONLYUSEDITISDIFFICULTTOESCAPETHECONCLUSIONTHATTHEMEANINGANDTHEANSWERTOTHEQUESTIONCANMACHINESTHINKISTOBESOUGHTINASTATISTICALSURVEYSUCHASAGALLUPPOLLBUTTHISISABSURDINSTEADOFATTEMPTINGSUCHADEFINITIONISHALLREPLACETHEQUESTIONBYANOTHERWHICHISCLOSELYRELATEDTOITANDISEXPRESSEDINRELATIVELYUNAMBIGUOUSWORDS'
    
    E = Enigma(0, [0, 3, 2], [17, 18, 14], [1, 4, 5], 'MA-RK-SD-JC-OB')
    p = 'ITWASABRIGHTCOLDDAYINAPRILANDTHECLOCKSWERESTRIKINGTHIRTEENWINSTONSMITHHISCHINNUZZLEDINTOHISBREASTINANEFFORTTOESCAPETHEVILEWINDSLIPPEDQUICKLYTHROUGHTHEGLASSDOORSOFVICTORYMANSIONSTHOUGHNOTQUICKLYENOUGHTOPREVENTASWIRLOFGRITTYDUSTFROMENTERINGALONGWITHHIMTHEHALLWAYSMELTOFBOILEDCABBAGEANDOLDRAGMATSATONEENDOFITACOLOUREDPOSTERTOOLARGEFORINDOORDISPLAYHADBEENTACKEDTOTHEWALLITDEPICTEDSIMPLYANENORMOUSFACEMORETHANAMETREWIDETHEFACEOFAMANOFABOUTFORTYFIVEWITHAHEAVYBLACKMOUSTACHEANDRUGGEDLYHANDSOMEFEATURESWINSTONMADEFORTHESTAIRSITWASNOUSETRYINGTHELIFTEVENATTHEBESTOFTIMESITWASSELDOMWORKINGANDATPRESENTTHEELECTRICCURRENTWASCUTOFFDURINGDAYLIGHTHOURSITWASPARTOFTHEECONOMYDRIVEINPREPARATIONFORHATEWEEKTHEFLATWASSEVENFLIGHTSUPANDWINSTONWHOWASTHIRTYNINEANDHADAVARICOSEULCERABOVEHISRIGHTANKLEWENTSLOWLYRESTINGSEVERALTIMESONTHEWAYONEACHLANDINGOPPOSITETHELIFTSHAFTTHEPOSTERWITHTHEENORMOUSFACEGAZEDFROMTHEWALLITWASONEOFTHOSEPICTURESWHICHARESOCONTRIVEDTHATTHEEYESFOLLOWYOUABOUTWHENYOUMOVEBIGBROTHERISWATCHINGYOUTHECAPTIONBENEATHITRANINSIDETHEFLATAFRUITYVOICEWASREADINGOUTALISTOFFIGURESWHICHHADSOMETHINGTODOWITHTHEPRODUCTIONOFPIGIRONTHEVOICECAMEFROMANOBLONGMETALPLAQUELIKEADULLEDMIRRORWHICHFORMEDPARTOFTHESURFACEOFTHERIGHTHANDWALLWINSTONTURNEDASWITCHANDTHEVOICESANKSOMEWHATTHOUGHTHEWORDSWERESTILLDISTINGUISHABLETHEINSTRUMENTTHETELESCREENITWASCALLEDCOULDBEDIMMEDBUTTHEREWASNOWAYOFSHUTTINGITOFFCOMPLETELYHEMOVEDOVERTOTHEWINDOWASMALLISHFRAILFIGURETHEMEAGRENESSOFHISBODYMERELYEMPHASIZEDBYTHEBLUEOVERALLSWHICHWERETHEUNIFORMOFTHEPARTYHISHAIRWASVERYFAIRHISFACENATURALLYSANGUINEHISSKINROUGHENEDBYCOARSESOAPANDBLUNTRAZORBLADESANDTHECOLDOFTHEWINTERTHATHADJUSTENDEDOUTSIDEEVENTHROUGHTHESHUTWINDOWPANETHEWORLDLOOKEDCOLDDOWNINTHESTREETLITTLEEDDIESOFWINDWEREWHIRLINGDUSTANDTORNPAPERINTOSPIRALSANDTHOUGHTHESUNWASSHININGANDTHESKYAHARSHBLUETHERESEEMEDTOBENOCOLOURINANYTHINGEXCEPTTHEPOSTERSTHATWEREPLASTEREDEVERYWHERETHEBLACKMOUSTACHIODFACEGAZEDDOWNFROMEVERYCOMMANDINGCORNERTHEREWASONEONTHEHOUSEFRONTIMMEDIATELYOPPOSITEBIGBROTHERISWATCHINGYOUTHECAPTIONSAIDWHILETHEDARKEYESLOOKEDDEEPINTOWINSTONSOWNDOWNATSTREETLEVELANOTHERPOSTERTORNATONECORNERFLAPPEDFITFULLYINTHEWINDALTERNATELYCOVERINGANDUNCOVERINGTHESINGLEWORDINGSOCINTHEFARDISTANCEAHELICOPTERSKIMMEDDOWNBETWEENTHEROOFSHOVEREDFORANINSTANTLIKEABLUEBOTTLEANDDARTEDAWAYAGAINWITHACURVINGFLIGHTITWASTHEPOLICEPATROLSNOOPINGINTOPEOPLESWINDOWSTHEPATROLSDIDNOTMATTERHOWEVERONLYTHETHOUGHTPOLICEMATTEREDBEHINDWINSTONSBACKTHEVOICEFROMTHETELESCREENWASSTILLBABBLINGAWAYABOUTPIGIRONANDTHEOVERFULFILMENTOFTHENINTHTHREEYEARPLANTHETELESCREENRECEIVEDANDTRANSMITTEDSIMULTANEOUSLYANYSOUNDTHATWINSTONMADEABOVETHELEVELOFAVERYLOWWHISPERWOULDBEPICKEDUPBYITMOREOVERSOLONGASHEREMAINEDWITHINTHEFIELDOFVISIONWHICHTHEMETALPLAQUECOMMANDEDHECOULDBESEENASWELLASHEARDTHEREWASOFCOURSENOWAYOFKNOWINGWHETHERYOUWEREBEINGWATCHEDATANYGIVENMOMENTHOWOFTENORONWHATSYSTEMTHETHOUGHTPOLICEPLUGGEDINONANYINDIVIDUALWIREWASGUESSWORKITWASEVENCONCEIVABLETHATTHEYWATCHEDEVERYBODYALLTHETIMEBUTATANYRATETHEYCOULDPLUGINYOURWIREWHENEVERTHEYWANTEDTOYOUHADTOLIVEDIDLIVEFROMHABITTHATBECAMEINSTINCTINTHEASSUMPTIONTHATEVERYSOUNDYOUMADEWASOVERHEARDANDEXCEPTINDARKNESSEVERYMOVEMENTSCRUTINIZEDWINSTONKEPTHISBACKTURNEDTOTHETELESCREENITWASSAFERTHOUGHASHEWELLKNEWEVENABACKCANBEREVEALINGAKILOMETREAWAYTHEMINISTRYOFTRUTHHISPLACEOFWORKTOWEREDVASTANDWHITEABOVETHEGRIMYLANDSCAPETHISHETHOUGHTWITHASORTOFVAGUEDISTASTETHISWASLONDONCHIEFCITYOFAIRSTRIPONEITSELFTHETHIRDMOSTPOPULOUSOFTHEPROVINCESOFOCEANIAHETRIEDTOSQUEEZEOUTSOMECHILDHOODMEMORYTHATSHOULDTELLHIMWHETHERLONDONHADALWAYSBEENQUITELIKETHISWERETHEREALWAYSTHESEVISTASOFROTTINGNINETEENTHCENTURYHOUSESTHEIRSIDESSHOREDUPWITHBAULKSOFTIMBERTHEIRWINDOWSPATCHEDWITHCARDBOARDANDTHEIRROOFSWITHCORRUGATEDIRONTHEIRCRAZYGARDENWALLSSAGGINGINALLDIRECTIONSANDTHEBOMBEDSITESWHERETHEPLASTERDUSTSWIRLEDINTHEAIRANDTHEWILLOWHERBSTRAGGLEDOVERTHEHEAPSOFRUBBLEANDTHEPLACESWHERETHEBOMBSHADCLEAREDALARGERPATCHANDTHEREHADSPRUNGUPSORDIDCOLONIESOFWOODENDWELLINGSLIKECHICKENHOUSESBUTITWASNOUSEHECOULDNOTREMEMBERNOTHINGREMAINEDOFHISCHILDHOODEXCEPTASERIESOFBRIGHTLITTABLEAUXOCCURRINGAGAINSTNOBACKGROUNDANDMOSTLYUNINTELLIGIBLETHEMINISTRYOFTRUTHMINITRUEINNEWSPEAKNEWSPEAKWASTHEOFFICIALLANGUAGEOFOCEANIAFORANACCOUNTOFITSSTRUCTUREANDETYMOLOGYSEEAPPENDIXWASSTARTLINGLYDIFFERENTFROMANYOTHEROBJECTINSIGHTITWASANENORMOUSPYRAMIDALSTRUCTUREOFGLITTERINGWHITECONCRETESOARINGUPTERRACEAFTERTERRACEMETRESINTOTHEAIRFROMWHEREWINSTONSTOODITWASJUSTPOSSIBLETOREADPICKEDOUTONITSWHITEFACEINELEGANTLETTERINGTHETHREESLOGANSOFTHEPARTYWARISPEACEFREEDOMISSLAVERYIGNORANCEISSTRENGTH'
    
    c = E(p)
    print(c)
    
    # IV I III
    # RSO
    # BEF
    # ma rk sd jc ob
    
    rotors, reflector, plugboard, rings, offsets = brute(c, range(5), 3, range(1), 5)[0]
    
    pp = Enigma(rotors, reflector, plugboard, rings, offsets)(c)
    
    print('=== Resulting plaintextish ===')
    print(pp)
    print('')
    print('=== Diff ===')
    print(''.join(x if x == y else '-' for x, y in zip(p, pp)))

