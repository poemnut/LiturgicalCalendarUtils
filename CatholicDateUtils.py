# -*- coding: cp1252 -*-

#----------------------------------------------------------------------------------#
# Catholic DateUtils
# https://github.com/MRNL-/LiturgicalCalendarUtils
# (C) Martin Raynal, 2015
#----------------------------------------------------------------------------------#
# The Calendar part of this module is inspired by and based on ROMCAL 6.2
# ROMCAL is Copyright (C) 1993-2003 Kenneth G. Bath (kbath@harris.com)
# See http://www.romcal.net/ for additional credits and informations
#----------------------------------------------------------------------------------#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>. 
#----------------------------------------------------------------------------------#

import calendar

from dateutil import rrule
from dateutil.easter import *
from datetime import date
from datetime import timedelta

from LiturgicalUtils import *

seatab=["Ordinary Time",
            "Advent",
            "Christmas",
            "Lent",
            "Easter"]
daytab=["",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]           
numtab = ["",
          "First",
          "Second",
          "Third",
          "Fourth",
          "Fifth",
          "Sixth",
          "Seventh",
          "Eighth",
          "Ninth",
          "Tenth",
          "Eleventh",
          "Twelfth",
          "Thirteenth",
          "Fourteenth",
          "Fifteenth",
          "Sixteenth",
          "Seventeenth",
          "Eighteenth",
          "Nineteenth"]
epbefore=["",
      "Monday before Epiphany",
      "Tuesday before Epiphany",
      "Wednesday before Epiphany",
      "Thursday before Epiphany",
      "Friday before Epiphany",
      "Saturday before Epiphany"]
epoctave=["",
      "Monday after Epiphany",
      "Tuesday after Epiphany",
      "Wednesday after Epiphany",
      "Thursday after Epiphany",
      "Friday after Epiphany",
      "Saturday after Epiphany"]

ep = "Epiphany of the Lord"
bl = "Baptism of the Lord"

ash_week=["Ash Wednesday",
      "Thursday after Ash Wednesday",
      "Friday after Ash Wednesday",
      "Saturday after Ash Wednesday"]
holy_week=["Palm Sunday",
      "Monday of Holy Week",
      "Tuesday of Holy Week",
      "Wednesday of Holy Week",
      "Holy Thursday",
      "Good Friday",
      "Easter Vigil"]

eaoctave=["Easter Sunday",
      "Monday in the Octave of Easter",
      "Tuesday in the Octave of Easter",
      "Wednesday in the Octave of Easter",
      "Thursday in the Octave of Easter",
      "Friday in the Octave of Easter",
      "Saturday in the Octave of Easter",
      "Second Sunday of Easter 'In Albis' - Divine Mercy Sunday"]
asc= "Ascension of the Lord";
pen = "Pentecost Sunday";
tri = "Trinity Sunday";
cc = "Corpus Christi";
shJ = "Sacred Heart of Jesus";
ihM = "Immaculate Heart of Mary";

ck = "Christ the King";

hf = "Holy Family"
cmoctave = ["Second day in the Octave of Christmas",
            "Third day in the Octave of Christmas",
            "Fourth day in the Octave of Christmas",
            "Fifth day in the Octave of Christmas",
            "Sixth day in the Octave of Christmas",
            "Seventh day in the Octave of Christmas"]

#===================================================

def IsEasterTide(date):
    "Returns TRUE if provided date is during Pascal Time."
    return (date >= easter(date.year) and date <= Trinity(date.year))

def IsHolyWeek(date):
    ""
    return (date > PalmSunday(date.year) and date < easter(date.year))

def IsInEasterOctave(date):
    ""
    d=timedelta(weeks=1)
    return (date >= easter(date.year) and date <= easter(year)+d)

def IsTriduum(date):
    ""
    return (date >= HolyThursday(date.year) and date < easter(date.year))

def IsLentTime(date):
    "Returns TRUE if provided date is during Lent. NOTE: this includes Sundays for now."
    #TODO? : check if not sunday ?
    return (date >= AshWednesday(date.year) and date < easter(date.year))

def IsAdventTime(date):
    "Returns TRUE if provided date is during Advent."
    return (date >= FirstSundayOfAdvent(date.year) and date < Christmas(date.year))

#======== LENT & PASCAL TIME ==================
def AshWednesday(year):
    "Ash Wednesday for given year. / Mercredi des Cendres de l'ann�e $year"
    d=timedelta(days=-46)
    return easter(year)+d

def PalmSunday(year):
    "Palm Sunday for given year. / Dimanche des Rameaux de l'ann�e year"
    d=timedelta(weeks=-1)
    return easter(year)+d

def HolyThursday(year):
    ""
    d=timedelta(days=-3)
    return easter(year)+d

def GoodFriday(year):
    ""
    d=timedelta(days=-2)
    return easter(year)+d

def EasterVigil(year):
    ""
    d=timedelta(days=-1)
    return easter(year)+d

def Easter(year):
    "Easter of given year. / Paques pour l'ann�e [year]"
    # Redefined to provide a consistent API
    return easter(year)

def Ascension(year):
    ""
    d=timedelta(days=39)
    return easter(year)+d

def Pentecost(year):
    "Whit Sunday of given year. / Pentecote"
    d=timedelta(weeks=7)
    return easter(year)+d

def Trinity(year):
    ""
    d=timedelta(days=56)
    return easter(year)+d

def CorpusChristi(year):
    ""
    # Saint-Sacrement (Fete-Dieu)
    d=timedelta(days=63)
    return easter(year)+d

def SacredHearth(year):
    ""
    d=timedelta(days=19)
    return Pentecost(year)+d

#======== ADVENT & CHRISTMAS ==================
def ChristKing(year):
    ""
    d=timedelta(weeks=-1)
    return FirstSundayOfAdvent(year)+d

def FirstSundayOfAdvent(year):
    ""
    weeks = 4;
    correction = 0;
    christmas = date(year, 12, 25)
    if (christmas.weekday() != 6) :
        # 6 is Sunday
        weeks-= 1
        correction = (christmas.isoweekday())
    d=timedelta(days=(-1*((weeks*7)+correction)))
    return christmas+d

def SecondSundayOfAdvent(year):
    ""
    d=timedelta(weeks=1)
    return FirstSundayOfAdvent(year)+d

def ThirdSundayOfAdvent(year):
    ""
    d=timedelta(weeks=2)
    return FirstSundayOfAdvent(year)+d

def FourthSundayOfAdvent(year):
    ""
    d=timedelta(weeks=3)
    return FirstSundayOfAdvent(year)+d

def Christmas(year):
    "...OK, this one was soooo hard."
    return date(year, 12, 25)

#======== SOLEMNITIES ========================
def Sol_MaryMotherOfGod(year):
    return date(year, 1, 1)

def Epiphany(year):
    ""
    #TODO fixed:  return date(year, 1, 6)
    #Sunday following Jan, 1st
    s = date(year, 1, 2)
    e = date(year, 1, 8)
    delta = timedelta(days=1)
    while s <= e:
        if(s.weekday()==6):
            return s
        s+=delta
    return e

def StJoseph(year):
    ""
    # TODO: Confirm rules
    joseph = date(year, 3, 19)
    # Anticipated to saturday 18 if 19 is Palm sunday & observed as a holy
    # day of obligation
    if(joseph == PalmSunday(year)):
        d = timedelta(days=-1)
        return joseph+d
    return joseph

def Annunciation(year):
    ""
    annonciation = date(year, 3, 25)
    easter_ = easter(year)
    
    # the second monday after easter if 25 is during holy week or Pascal week
    if(easter_<=date(year,4,2)):
        d = timedelta(weeks=1, days=1)
        return easter_+d
    
    # the following monday if 25/03 is a sunday
    if(annonciation.weekday()==6):
        d = timedelta(days=1)
        return annonciation+d
        
    return annonciation

def Sol_NativityOfJohnTheBaptist(year):
    return date(year, 6, 24)

def StsPeterAndPaul(year):
    return date(year, 6, 29)

def Assumption(year):
    return date(year, 8, 15)

def AllSaints(year):
    return date(year, 11, 1)

def ImmaculateConception(year):
    return date(year, 12, 8)

#======== FEASTS ========================
# Feast are superseded by sundays except for Feasts of the Lord & All Souls

def ConversionOfPaul(year):
    paul_cv = date(year, 1, 25)
    if(paul_cv.weekday() == 6):
        return
    return paul_cv

def PresentationOfTheLord(year):
    "Pr�sentation de J�sus au Temple"
    return date(year, 2, 2)

def ChairOfPeter(year):
    chair = date(year, 2, 22)
    if(chair.weekday() == 6):
        return
    return chair

def StMarkEvangelist(year):
    mark = date(year, 4, 25)
    if(mark.weekday() == 6):
        return
    return mark

def StsPhilipAndJames(year):
    "Saints Jacques et Philippe, apotres"
    pAj = date(year, 5, 3)
    if(pAj.weekday() == 6):
        return
    return pAj

# TODO check what to do if any solemnity falls the same day
# i.e. 14/05/2015 was Ascension Thursday...
def StMatthias(year):
    "Saint Matthias, apotre"
    pAj = date(year, 5, 14)
    if(pAj.weekday() == 6):
        return
    return pAj

def Visitation(year):
    visitation = date(year, 5, 31)
    if(visitation.weekday() == 6):
        return
    return visitation

def StThomas(year):
    thomas = date(year, 7, 3)
    if(thomas.weekday() == 6):
        return
    return thomas

def StJames(year):
    "Saint Jacques le Majeur"
    james = date(year, 7, 3)
    if(james.weekday() == 6):
        return
    return james

def Transfiguration(year):
    return date(year, 8, 6)   

def StLawrence(year):
    "Saint Laurent"
    lt = date(year, 8, 10)
    if(lt.weekday() == 6):
        return
    return lt

def StBartholomew(year):
    "Saint Barthelemy"
    bt = date(year, 8, 24)
    if(bt.weekday() == 6):
        return
    return bt

def BirthOfMary(year):
    "Nativite de la Vierge Marie"
    bm = date(year, 9, 8)
    if(bm.weekday() == 6):
        return
    return bm

def Transfiguration(year):
    return date(year, 9, 14)

def StMatthew(year):
    "Saint Matthieu Evangeliste"
    mt = date(year, 9, 21)
    if(mt.weekday() == 6):
        return
    return mt

def Archangels(year):
    "Saints Archanges Michel, Gabriel & Raphael"
    a = date(year, 9, 29)
    if(a.weekday() == 6):
        return
    return a

def StLuke(year):
    "Saint Luc evangeliste"
    luke = date(year, 10, 18)
    if(luke.weekday() == 6):
        return
    return luke

def StsSimonAndJude(year):
    "Saints Simon & Jude, apotres"
    sj = date(year, 10, 28)
    if(sj.weekday() == 6):
        return
    return sj

def AllSouls(year):
    "D�funts"
    return date(year, 11, 2)

def DedicationOfStJohnLateran(year):
    "Dedicace de la basilique St-Jean-de-Latran"
    return date(year, 11, 9)

def StAndrew(year):
    "Saint Andre, apotre"
    a = date(year, 11, 30)
    if(a.weekday() == 6):
        return
    return a

def StStephen(year):
    "Saint Etienne, martyr"
    s = date(year, 12, 26)
    if(s.weekday() == 6):
        return
    return s

def StJohn(year):
    "Saint Jean, evangeliste"
    j = date(year, 12, 27)
    if(j.weekday() == 6):
        return
    return j

def StsInnocents(year):
    "Saints Innocents, martyrs"
    i = date(year, 12, 28)
    if(i.weekday() == 6):
        return
    return i

#----- Mobile feasts --------------

def HolyFamily(year):
    "Fete de la Sainte-Famille"
    if(Christmas(year).weekday() == 6):
        return date(year, 12, 30)
    day = (Christmas(year).isoweekday())
    d=timedelta(days=(7 - day))
    return christmas+d

# Todo: if epiphany is fixed to 6/1
def BaptismOfTheLord(year):
    d=timedelta(weeks=1)
    return Epiphany(year)+d

#=====================================

def StMartin(year):
    "St Martin de Tours"
    return date(year, 11, 11)





#==========================================
#==========================================
#  MAIN
#==========================================
#==========================================
def genCelebration(season, week, dow):
    "Returns the general name of a celebration given a season, a week number, and a day of the week"

    numstring=None
    retval=""

    # Week number
    if (week == 20):
           numstring="Twentieth"
    elif (week == 30):
           numstring="Thirtieth"
    elif (week > 30):
           numstring="Thirty-" + numtab[week % 10]
    elif (week > 20):
           numstring="Twenty-" + numtab[week % 10]
    else:
           numstring=numtab[week]

    #special case for sunday
    if (dow == 7):
           retval += numstring + " Sunday of " + seatab[season.value]
    else:
           retval += daytab[dow] + " of the " + numstring + " Week of " + seatab[season.value]

    return retval



def computeCalendar(year):
    "Compute the whole calendar for given year"
    numdays=365
    if(calendar.isleap(year)):
       numdays=366

    #init the calendar
    cal=[]
    yeardates=list(rrule.rrule(rrule.DAILY,dtstart=date(year,1,1),until=date(year,12,31)))
    for d in yeardates:
        rk=Ranks.WEEKDAY
        if(d.isoweekday()==7):
            rk=Ranks.SUNDAY
            
        cal.append(LiturgicalDay(d, Colors.GREEN, rk, Seasons.ORDINARY, None))

    #= Christmas Time == from the start of the year ================
    # -- Days before Epiphany
    for day in cal[0:5]:        
        day.season = Seasons.CHRISTMAS
        day.color = Colors.WHITE
        dow = day.date.isoweekday()  
        #Second Sunday of Christmas
        if(dow==7):
            day.descr=genCelebration(Seasons.CHRISTMAS, 2, dow)
        else:
            day.descr=epbefore[dow]

    # -- Epiphany
    epi=cal[5]
    epi.descr=ep
    epi.season = Seasons.CHRISTMAS
    epi.color = Colors.WHITE
    epi.rank=Ranks.SOLEMNITY

    # ---- get sunday after epiphany (day of Baptism of the Lord)
    bld= 12-epi.date.isoweekday()
    
    # -- Days after Epiphany
    for day in cal[6:bld]:
        dow = day.date.isoweekday()
        day.season = Seasons.CHRISTMAS
        day.color = Colors.WHITE
        day.descr=epoctave[dow]
    
    # -- Baptism of the Lord 
    bL=cal[bld]
    bL.descr=bl
    bL.season = Seasons.CHRISTMAS
    bL.color = Colors.WHITE
    bL.rank=Ranks.LORD

    #= Lent ========================================================
    # ---- get Easter day of year
    iaw=AshWednesday(year).timetuple().tm_yday - 1

    # -- Ash Wednesday and following week
    for i,day in enumerate(cal[iaw:iaw+4]):
        day.descr = ash_week[i]
        day.color = Colors.PURPLE

        if(day.date.isoweekday()==3):
            day.rank = Ranks.ASHWED
            day.season = Seasons.LENT
        else:
            day.rank = Ranks.WEEKDAY
            day.season = Seasons.LENT

    # -- First sunday of Lent
    lent1 = iaw+4
    lt1=cal[lent1]
    lt1.descr=genCelebration(Seasons.LENT, 1, 7)
    lt1.season = Seasons.LENT
    lt1.color = Colors.PURPLE
    
    # -- Palm Sunday
    palm=PalmSunday(year).timetuple().tm_yday - 1    
    plm=cal[palm]
    plm.descr=holy_week[0]
    plm.season = Seasons.PASSION
    plm.color = Colors.RED

    # -- Fill Lent season up to Palm Sunday
    # ---- begin on first monday of Lent
    week = 1
    dow = 1
    for i,day in enumerate(cal[lent1+1:palm]):
        day.descr=genCelebration(Seasons.LENT, week, dow)
        day.season = Seasons.LENT

        if(i==20): #Laetare
            day.color=Colors.ROSE
        else:
            day.color=Colors.PURPLE
        
        dow = (dow+1)% 8
        if dow == 7:
            week+=1
        if dow == 0:
            #start of secular week is monday, 1 in iso
            dow+=1

    # -- Fill the Holy Week
    hw_colors=[Colors.RED,
               Colors.PURPLE, Colors.PURPLE, Colors.PURPLE,
               Colors.WHITE, Colors.RED, Colors.WHITE]
    hw_ranks=[Ranks.SUNDAY,
             Ranks.HOLYWEEK, Ranks.HOLYWEEK, Ranks.HOLYWEEK,
             Ranks.TRIDUUM, Ranks.TRIDUUM, Ranks.TRIDUUM]
    dow=1
    
    for day in cal[palm+1:palm+7]:
        day.descr = holy_week[dow]
        day.season = Seasons.PASSION
        day.color = hw_colors[dow]
        day.rank = hw_ranks[dow]
        dow+=1
        
    #= Paschal & Easter time =======================================
    # -- EASTER
    easter=Easter(year).timetuple().tm_yday - 1    
    easterS=cal[easter]
    easterS.descr=eaoctave[0]
    easterS.season = Seasons.PASCHAL
    easterS.rank=Ranks.SOLEMNITY
    easterS.color = Colors.GOLD

    dow=1
    # ---- Octave of Easter
    for day in cal[easter+1:easter+8]:
        day.descr = eaoctave[dow]
        day.season = Seasons.PASCHAL
        day.color = Colors.WHITE
        day.rank = Ranks.SOLEMNITY
        dow+=1

    # -- Pentecost Sunday
    pentecost=easter+49
    ps = cal[pentecost]
    ps.descr = pen
    ps.season = Seasons.EASTER
    ps.color = Colors.RED
    ps.rank = Ranks.SOLEMNITY

    # -- Easter Season
    dow=1
    week=2
    for day in cal[easter+8:pentecost]:
        day.descr = genCelebration(Seasons.EASTER, week, dow)
        day.season = Seasons.EASTER
        day.color = Colors.WHITE

        dow = (dow+1)% 8
        if dow == 7:
            week+=1
        if dow == 0:
            #start of secular week is monday, 1 in iso
            dow+=1

    # -- Ascension Thursday
    ast=easter+39
    at = cal[ast]
    at.descr = asc
    at.season = Seasons.EASTER
    at.color = Colors.WHITE
    at.rank = Ranks.SOLEMNITY
    
    # -- Trinity Sunday
    tns=easter+56
    trinity = cal[tns]
    trinity.descr = tri
    trinity.season = Seasons.ORDINARY
    trinity.color = Colors.WHITE
    trinity.rank = Ranks.SOLEMNITY
    
    # -- Corpus Christi
    # ---- fall on Sunday in France
    ccd=easter+63
    corpusC = cal[ccd]
    corpusC.descr = cc
    corpusC.season = Seasons.ORDINARY
    corpusC.color = Colors.WHITE
    corpusC.rank = Ranks.SOLEMNITY
    
    # -- Sacred Heart
    ccd=easter+68
    corpusC = cal[ccd]
    corpusC.descr = shJ
    corpusC.season = Seasons.ORDINARY
    corpusC.color = Colors.WHITE
    corpusC.rank = Ranks.SOLEMNITY
    
    # -- Immaculate Heart of Mary
    ihd=easter+69
    imHM = cal[ihd]
    imHM.descr = ihM
    imHM.season = Seasons.ORDINARY
    imHM.color = Colors.WHITE
    imHM.rank = Ranks.MEMORIAL

    #= Advent ======================================================
    # ---- Lenght of advent season indexed by Christmas DayOfWeek
    # ------ (Sunday=0 or 7)
    adventLen=[28,22,23,24,25,26,27,28]

    # ---- Christmas day of year & week
    cdoy=Christmas(year).timetuple().tm_yday - 1 
    cdow=Christmas(year).isoweekday()

    # -- First Sunday of Advent
    advent1=cdoy-adventLen[cdow]
    adv1=cal[advent1]
    adv1.descr=genCelebration(Seasons.ADVENT, 1, 7)
    adv1.season = Seasons.ADVENT
    adv1.color = Colors.PURPLE

    # -- Christ the King
    ckd=cal[advent1-7]
    ckd.descr=ck
    ckd.season = Seasons.ORDINARY
    ckd.color = Colors.WHITE
    ckd.rank = Ranks.SOLEMNITY
    
    # -- Fill Advent season
    week = 1
    dow = 1
    for i,day in enumerate(cal[advent1+1:cdoy]):
        day.descr=genCelebration(Seasons.ADVENT, week, dow)
        day.season = Seasons.ADVENT
        if(i==13): #Gaudete
            day.color=Colors.ROSE
        else:
            day.color=Colors.PURPLE
        
        dow = (dow+1)% 8
        if dow == 7:
            week+=1
        if dow == 0:
            #start of secular week is monday, 1 in iso
            dow+=1


    #= Christmas Time ==============================================    
    # -- Fill the week following Christmas.
    # ---- The Sunday between Dec. 26 and Dec.31 is Holy Family    
    dec26=cdoy+1
    for i,day in enumerate(cal[dec26:]):
        
        day.season = Seasons.CHRISTMAS
        day.color = Colors.WHITE
        
        dow=day.date.isoweekday()        
        if(dow==7):
            day.descr = hf
            day.rank = Ranks.LORD
        else:
            day.descr = cmoctave[i]

    # ---- If Christmas falls on a Sunday, Holy Family is celebrated on Dec. 30.
    if(cdow==7):
        dec30=HolyFamily(year).timetuple().tm_yday - 1
        hfd=cal[dec30]
        hfd.descr = hf
        hfd.rank = Ranks.LORD
        hfd.season = Seasons.CHRISTMAS
        hfd.color = Colors.WHITE

    #TODO !!! Fixed celebrations & stuff
    #proper()


    #= Ordinary Time ===============================================
    # -- First part
    week=1
    for day in cal[bld+1:iaw]:
        dow=day.date.isoweekday()
        if(day.rank==Ranks.WEEKDAY or
           (dow== 7 and day.rank.value<Ranks.LORD.value)):
            day.descr=genCelebration(Seasons.ORDINARY, week, dow)
            day.season = Seasons.ORDINARY
            day.color = Colors.GREEN
            
            if dow == 6:
                week+=1
    
    # -- Second part
    # ---- The last week of Ordinary Time is always the 34th Week of Ordinary Time.
    week=35
    for day in reversed(cal[pentecost:advent1]):        
        dow=day.date.isoweekday()
        if dow == 6:
            week-=1
        if(day.rank==Ranks.WEEKDAY or
           (dow== 7 and day.rank.value<Ranks.LORD.value)):
            day.descr=genCelebration(Seasons.ORDINARY, week, dow)
            day.season = Seasons.ORDINARY
            day.color = Colors.GREEN
                
    return cal






#load properties
#myprops = dict(line.strip().split('=') 
#               for line in open('/Path/filename.properties'))
#               if ("=" in line and 
#                   not line.startswith("#")))
 #     print day.date.date(), day.color, day.rank, day.descr, day.season   
       
