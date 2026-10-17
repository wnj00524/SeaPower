"""Compile authored narrative into Sea Power briefing panels and tactical charts.

Pillow is needed only when regenerating committed charts. Charts show friendly
planning data, never enemy spawn positions. They are not navigation products.
"""
import datetime
import json
import math
import os
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont
from validate_scenarios import ROOT, POLYGONS, read, position

BASE = ROOT / 'campaign/user/Operation_Broken_Trident/campaigns/operation-broken-trident'
ASSETS = BASE / 'briefing_assets'
TEXT = json.loads((ROOT / 'briefing_source/missions.json').read_text())
NAVY, PANEL, LAND, COAST = '#0b1824', '#102536', '#344942', '#a4b39d'
WHITE, MUTED, CYAN, GOLD = '#f0eee4', '#b1c1cd', '#72d5df', '#e8bb72'


def font(size, bold=False):
    suffix = '-Bold' if bold else ''
    candidates=[f'DejaVuSans{suffix}.ttf',f'/usr/share/fonts/truetype/dejavu/DejaVuSans{suffix}.ttf',str(Path(os.environ.get('WINDIR','C:/Windows'))/'Fonts'/('arialbd.ttf' if bold else 'arial.ttf'))]
    for candidate in candidates:
        try:return ImageFont.truetype(candidate,size)
        except OSError:pass
    raise SystemExit('Install DejaVu Sans or Arial before rebuilding charts.')


def write_ini(path, c):
    import io
    out = io.StringIO()
    c.write(out, space_around_delimiters=False)
    path.write_text(out.getvalue().rstrip()+'\n', encoding='utf-8')


def geo(u, center):
    return position(u['GeoPosition'], center, True)


def chart(path, c, entry, objective):
    image = Image.new('RGB', (1440, 1008), NAVY)
    d = ImageDraw.Draw(image)
    title = c['Language_en']['Name'].upper()
    d.text((44,25),'SIXTH FLEET  /  OPERATIONS',font=font(18,True),fill=GOLD)
    d.text((44,59),title,font=font(34,True),fill=WHITE)
    d.text((44,111),entry['subtitle'].upper(),font=font(18),fill=MUTED)
    center=tuple(float(c['Environment'][k]) for k in ('MapCenterLatitude','MapCenterLongitude'))

    def panel(box, bounds):
        x0,y0,x1,y1=box
        w,h=x1-x0,y1-y0
        layer=Image.new('RGB',(w,h),PANEL);p=ImageDraw.Draw(layer)
        lon0,lat0,lon1,lat1=bounds
        cosine=math.cos(math.radians((lat0+lat1)/2))
        scale=min((w-34)/((lon1-lon0)*cosine),(h-30)/(lat1-lat0))
        def xy(lat,lon):
            return (w/2+(lon-(lon0+lon1)/2)*cosine*scale,h/2-(lat-(lat0+lat1)/2)*scale)
        for lon in range(math.floor(lon0),math.ceil(lon1)+1):
            a,b=xy(lat0,lon),xy(lat1,lon);p.line((a,b),fill='#203a4b',width=1)
            if 10<a[0]<w-55:p.text((a[0]+3,h-22),f'{lon}E',font=font(12),fill=MUTED)
        for lat in range(math.floor(lat0),math.ceil(lat1)+1):
            a,b=xy(lat,lon0),xy(lat,lon1);p.line((a,b),fill='#203a4b',width=1)
            if 8<a[1]<h-28:p.text((6,a[1]+2),f'{lat}N',font=font(12),fill=MUTED)
        for poly in POLYGONS:
            p.polygon([xy(lat,lon) for lon,lat in poly[0]],fill=LAND,outline=COAST,width=1)
            for ring in poly[1:]:p.polygon([xy(lat,lon) for lon,lat in ring],fill=PANEL)
        image.paste(layer,(x0,y0));d.rectangle(box,outline='#426175',width=1)
        return lambda lat,lon:(xy(lat,lon)[0]+x0,xy(lat,lon)[1]+y0),scale

    d.text((44,157),'THEATRE CONTEXT',font=font(17,True),fill=GOLD)
    project,_=panel((44,188,1396,530),(10.5,30.0,37.0,38.6))
    for label,lat,lon in [('SICILY',37.5,14),('CRETE',35.1,25),('CYPRUS',35.9,33.3),('LIBYA',31.3,18),('IONIAN SEA',36.2,19)]:
        x,y=project(lat,lon);d.text((x,y),label,font=font(15,True),fill=MUTED,anchor='mm')
    x,y=project(*center);d.ellipse((x-12,y-12,x+12,y+12),outline=GOLD,width=3)
    d.text((x+18,y+14),'OPERATING AREA',font=font(14,True),fill=GOLD)
    air=geo(c['Taskforce1LandUnit1'],center);x,y=project(*air)
    d.polygon([(x,y-8),(x-8,y+7),(x+8,y+7)],fill=CYAN)
    d.text((x+14,y+14 if entry['id']==7 else y-20),c['Language_en']['Taskforce1LandUnit1ShortNameOverride'],font=font(14,True),fill=CYAN)
    d.text((44,551),'LOCAL TASK  /  FRIENDLY PLANNING DATA',font=font(17,True),fill=GOLD)
    local,scale=panel((44,584,950,906),(center[1]-.78,center[0]-.66,center[1]+.88,center[0]+.6))
    x,y=local(*geo(c['Taskforce1Vessel1'],center))
    d.polygon([(x,y-9),(x-8,y+7),(x+8,y+7)],fill=CYAN)
    d.text((x-150,y-25),'TASK GROUP',font=font(14,True),fill=CYAN)
    t=c['Trigger3']
    if t['Condition_Type']=='UnitsInTheArea':
        u=c['NeutralVessel1'];start=geo(u,center)
        endpoint=position(t['Condition_PositionNM'],center)
        a,b=local(*start),local(*endpoint)
        d.line((a,b),fill=CYAN,width=4)
        angle=math.atan2(b[1]-a[1],b[0]-a[0])
        d.polygon([b,(b[0]-14*math.cos(angle-.45),b[1]-14*math.sin(angle-.45)),(b[0]-14*math.cos(angle+.45),b[1]-14*math.sin(angle+.45))],fill=CYAN)
        radius=float(t['Condition_AreaRadiusNM'])*scale/60
        x,y=b;d.ellipse((x-radius,y-radius,x+radius,y+radius),outline=GOLD,width=3)
        d.text((a[0]-10,a[1]-29),'PROTECTED SHIP',font=font(14,True),fill=WHITE)
        d.text((x-34,y-radius-23),'SAFETY AREA',font=font(14,True),fill=GOLD)
    else:
        x,y=local(*center)
        d.ellipse((x-70,y-70,x+70,y+70),outline=GOLD,width=2)
        label='SEARCH AREA' if entry['id'] in (2,4) else ('HOLDING TASK' if entry['id']==6 else 'SURFACE TASK')
        d.text((x-58,y+83),label,font=font(14,True),fill=GOLD)
        d.text((x-83,y-19),'NO CONFIRMED',font=font(15),fill=WHITE)
        d.text((x-83,y+4),'ENEMY POSITIONS',font=font(15),fill=WHITE)
    # North arrow is geographic. The local circle is an orientation symbol,
    # not an additional scripted search/picket constraint.
    d.line((914,641,914,610),fill=WHITE,width=2)
    d.polygon([(914,604),(908,616),(920,616)],fill=WHITE)
    d.text((908,589),'N',font=font(13,True),fill=WHITE)
    x,y=985,588
    for heading,body in [('PRIMARY TASK',objective),('CONTACT DISCIPLINE','Identify before firing. Merchant and fishing traffic remains neutral.'),('INTELLIGENCE','Threat types are assessed. Enemy locations are deliberately omitted.')]:
        d.text((x,y),heading,font=font(15,True),fill=GOLD);y+=28
        for line in textwrap.wrap(body,width=34):
            d.text((x,y),line,font=font(16),fill=WHITE);y+=23
        y+=20
    d.text((44,930),'CYAN  FRIENDLY / ASSIGNED TRACK       AMBER  TASK AREA',font=font(15,True),fill=MUTED)
    d.text((44,961),'FICTIONAL CAMPAIGN  |  Not for navigation. Enemy fixes omitted. Only escort safety circles are scripted boundaries.',font=font(14),fill=MUTED)
    temporary=path.with_suffix('.tmp.png')
    image.save(temporary,optimize=True)
    with Image.open(temporary) as check:check.load()
    temporary.replace(path)


def block(heading,text):
    return f'<TextBlock Text="{escape(heading, {chr(34): "&quot;"})}" Foreground="#E8BB72" FontSize="18" FontWeight="Bold" Margin="0,16,0,6"/><TextBlock Text="{escape(text, {chr(34): "&quot;"})}" TextWrapping="Wrap" FontSize="16" Foreground="#F0EEE4"/>'


def build():
    ASSETS.mkdir(exist_ok=True)
    campaign_path=BASE/'campaign.ini';campaign=read(campaign_path)
    for entry in TEXT:
        n=entry['id'];path=next((BASE/'missions').glob(f'{n:02} *.ini'));c=read(path);lang=c['Language_en'];t=c['Trigger3']
        phase=(n-1)//4+1
        dt=datetime.datetime(*map(int,c['Environment']['Date'].split(',')),*map(int,c['Environment']['Time'].split(',')))
        window=int(c['Trigger4']['Condition_Time'])//60
        if t['Condition_Type']=='UnitsInTheArea':
            ship=lang['NeutralVessel1NameOverride']
            objective=f'Keep {ship} afloat and bring her into the marked safety area within {window} minutes. Preserve at least one task-group vessel.'
            chart_objective=f'Escort {ship} to the safety area. Limit: {window} min.'
        elif n==6:
            objective='Keep at least one task-group vessel alive until 75 minutes have elapsed. No geographic station-keeping or enemy-kill condition is scripted.'
            chart_objective='Survive 75 minutes. No compulsory pursuit or station boundary.'
        else:
            names={2:'the designated Foxtrot submarine',4:'the designated Kilo submarine',5:'the designated Kashin and Krivak',9:'the Slava cruiser and designated Krivak escort',10:'the designated Udaloy, Kara and Krivak',12:'the Slava, Kara and designated Krivak'}
            objective=f'Destroy {names[n]} within {window} minutes. Preserve at least one task-group vessel. Additional escorts and shore sites are not compulsory targets.'
            chart_objective=f'Destroy {names[n]}. Limit: {window} min.'
        support=campaign[f'Mission{n}']
        logistics=('Rearm and repair are offered before this mission.' if support['TaskForceModeRearm']=='True' else 'No pre-mission rearm or repair is offered for this sortie.')
        logistics+=' Use '+lang['Taskforce1LandUnit1NameOverride']+' for aircraft you have purchased, assigned and prepared. No free friendly combat aircraft are promised. Ships and ammunition state carry through the campaign.'
        roe='Positive identification is required before attacking surface contacts. Hostile aircraft, missiles and positively identified enemy combatants may be engaged in defence of the task. Radar silence, nationality or proximity to a warship alone does not establish hostile intent. Protect the assigned transport where present; do not attack neutral traffic.'
        conditions=f'{dt:%d %B %Y, %H:%M}Z. Sea state {c["Environment"]["SeaState"]}; {c["Environment"]["Clouds"].lower()} cloud; wind from {c["Environment"]["WindDirection"]}. This is a fictional 1985 crisis. Doctrine guidance is advisory; completion conditions are stated explicitly above.'
        sections=[('COMMANDER\'S DISPATCH',entry['dispatch']),('SITUATION',entry['situation']),('MISSION / COMPLETION CONDITIONS',objective),('THREAT ASSESSMENT',entry['intelligence']),('EXECUTION',entry['execution']),('RULES OF ENGAGEMENT',roe),('AVIATION / SUSTAINMENT',logistics),('CONDITIONS / NOTES',conditions)]
        folder=BASE/'missions'/(path.stem+'_Briefing');folder.mkdir(exist_ok=True)
        basepath='campaigns/operation-broken-trident/'
        lang['MissionBriefingAssetsDirectory']=basepath+'briefing_assets'
        lang['MissionBriefingAssetsSearchPattern']='*.png,*.jpg'
        lang['MissionBriefingLeftPane']=basepath+'missions/'+folder.name+'/LeftPane_en.xml'
        lang['MissionBriefingRightPane']=basepath+'missions/'+folder.name+'/RightPane_en.xml'
        header=block(lang['Name'],entry['subtitle'])
        left='<ScrollViewer xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" VerticalScrollBarVisibility="Auto" HorizontalScrollBarVisibility="Disabled"><StackPanel Margin="20">'+header+f'<Image Source="{{Binding Assets[phase{phase}]}}" Stretch="Uniform" MaxHeight="240" Margin="0,16,0,4"/><TextBlock Text="Campaign illustration — fictional scene, not reconnaissance imagery." FontSize="12" TextWrapping="Wrap" Foreground="#B1C1CD"/>'+''.join(block(h,b) for h,b in sections)+'</StackPanel></ScrollViewer>\n'
        right=f'<Viewbox xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" Margin="12" Stretch="Uniform"><Canvas Width="1440" Height="1008"><Image Width="1440" Height="1008" Source="{{Binding Assets[chart{n:02}]}}"/></Canvas></Viewbox>\n'
        (folder/'LeftPane_en.xml').write_text(left)
        (folder/'RightPane_en.xml').write_text(right)
        lang['Taskforce1StartMessage']='|'.join([f'<color=yellow>{lang["Name"]} — {entry["subtitle"]}</color>',entry['dispatch'],objective,'ROE: identify surface contacts before firing. Civilian traffic remains in the area.',logistics])
        lang['Taskforce1VictoryMessage']='<color=lime>Task complete.</color>|'+entry['success']+'|'+('Operation Broken Trident concluded.' if n==12 else 'Surviving ships and recorded weapon state carry forward.')
        lang['Taskforce1DefeatMessage']='<color=red>Task failed.</color>|'+entry['failure']
        if 'Taskforce1CivilianLossMessage' in lang:lang['Taskforce1CivilianLossMessage']='<color=red>Protected ship lost.</color>|'+entry['failure']
        lang['Objective_Primary']=chart_objective
        if n==11:lang['Description']=lang['Description'].replace('west across','east through')
        campaign[f'Mission{n}']['Description_en']=lang['Description']+' '+entry['dispatch']
        write_ini(path,c)
        markdown=f'# {lang["Name"]}\n\n*{entry["subtitle"]}*\n\n'
        markdown+='\n\n'.join('## '+h+'\n\n'+b for h,b in sections)+'\n'
        (folder/'Orders_en.md').write_text(markdown)
        chart(ASSETS/f'chart{n:02}.png',c,entry,chart_objective)
        print(f'{n:02}: briefing, chart and narrative compiled')
    write_ini(campaign_path,campaign)


if __name__=='__main__':build()
