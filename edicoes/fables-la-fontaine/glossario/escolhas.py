E = {}
def e(pasta, s):
    d = E.setdefault(pasta, {})
    for par in s.split():
        ref, k = par.split('=')
        d[ref] = k
e('la-cigale-et-la-fourmi', '2.1=tout#2 19.5=tout#3 17.1=que#4 16.3=là#2 20.3=ne#2 4.4=fut#2 1.3=ayant#2 9.3=de#2')
e('le-corbeau-et-le-renard', '6.1=que#3 6.5=que#3 13.10=monsieur#2 15.1=vit#2 16.4=bien#2 18.12=plus 4.5=près#2 4.4=peu#2 10.10=de 14.3=tout#3')
e('la-grenouille-et-le-boeuf', '0.5=veut#2 0.9=que#5 3.7=en#4 3.8=tout 7.2=assez#3 7.7=suis#2 8.6=point#2 8.7=du#3 8.8=tout#5 11.12=sages#2 12.1=tout#3 13.1=tout#3 14.1=tout#3')
e('le-loup-et-le-chien', '1.5=que#6 3.8=que#5 4.5=était#2 6.1=sire#2 6.5=fait#3 8.6=taille#2 9.1=à#2 11.1=entre#2 13.1=il#2 13.4=qu’#4 13.8=sire#3 14.5=que#5 19.2=quoi#4 21.5=bien#4 22.4=que#4 22.7=il#2 25.7=maître#2 26.2=quoi#2 27.2=force#2 31.3=fait#2 33.1=qu’#3 33.3=là#2 33.8=quoi#5 33.12=chose#2 34.2=encor#2 37.7=qu’#3 38.2=importe#2 38.7=tous#2 40.5=même#3 40.8=prix#2 41.2=dit#2')
e('le-rat-de-ville-et-le-rat-des-champs', '0.4=ville#2 1.5=ville#2 15.4=ville#2 6.4=trouva#2 7.6=vie#2 8.1=que#2 12.1=pendant#2 18.1=rat#2 19.5=dire#3 20.2=tout#2 21.3=assez#4 24.2=tous#2 25.5=vient#3 26.2=mange#2 26.4=à#3 28.1=que#2 28.4=peut#3')
e('le-loup-et-l-agneau', '1.5=fort#2 2.5=tout#4 5.4=à#3 6.2=que#2 7.1=qui#2 10.5=que#7 12.3=qu’#7 12.4=elle#2 17.3=puis#2 20.5=fait#4 22.2=ce#3 23.5=point#3 23.10=des#2 24.2=vous#3 25.1=vous#3 26.4=a#3 26.5=dit#2 28.8=mange#3')
e('le-chene-et-le-roseau', '1.4=jour#2 2.2=avez#3 2.3=bien#2 4.2=moindre#2 4.6=aventure#2 5.1=fait#2 7.1=cependant#2 11.1=encor#3 13.3=auriez#2 17.7=bien#2 19.7=quittez#3 28.7=plie#2 24.5=comme#2 27.1=que#2 27.4=eût#2 28.2=arbre#2 28.3=tient#3 31.3=qui#3 31.7=ciel#3 31.9=voisine#2')
e('le-lion-et-le-rat', '1.8=tout#2 1.10=monde#2 2.9=que#5 3.7=foi#2 6.6=assez#2 7.2=roi#2 11.7=eût#3 12.1=cependant#3 12.7=des#2 15.1=sire#2 16.6=tout#2 18.4=force#3 18.6=que#5 18.7=rage#2 9.4=fut#2')
e('le-laboureur-et-ses-enfants', '1.3=de#5 4.2=fit#2 0.5=enfants#2 4.4=enfants#2 6.1=que#2 7.3=est#2 9.7=viendrez#2 9.9=bout#2 10.8=fait#3 10.9=août#2 13.3=mort#3 13.6=vous#2 14.8=bout#2 16.5=caché#2 16.10=sage#2 17.1=de#2 17.3=montrer#2')
e('le-lievre-et-la-tortue', '1.10=point#4 4.2=que#5 4.4=ce#2 4.7=êtes#3 4.9=sage#3 8.1=sage#3 8.6=encore#2 9.3=fait#5 11.8=affaire#2 13.5=que#6 13.6=quatre#2 13.7=pas#2 14.5=qu’#2 14.9=près#3 15.4=des#2 16.3=fait#2 17.4=du#2 19.3=vient#2 20.3=train#2 23.1=lui#2 24.1=tient#2 25.5=va#2 28.1=qu’#5 29.3=autre#2 32.9=raison#2 33.2=quoi#2 33.4=sert#2 34.5=que#4')
e('les-animaux-malades-de-la-peste', '1.2=mal#3 2.4=ciel#2 16.5=ciel#2 7.8=étaient#2 14.1=plus 14.5=plus 15.3=tint#2 16.6=a#2 18.1=que#7 21.7=de#4 22.3=de#4 26.2=ai#2 26.4=force#2 27.1=que#4 27.3=avaient#2 27.5=fait#3 28.4=est#2 30.6=il#2 30.7=le#3 31.3=est#3 31.5=que#7 31.10=que#5 35.3=font#2 35.6=de#3 38.1=en#3 38.6=honneur#2 40.6=tous#2 42.5=empire#2 44.4=trop#2 45.8=des#2 47.1=tous#2 48.2=dire#4 48.6=de#4 49.3=vint#2 51.4=occasion#2 51.10=pense#2 56.3=quelque#2 58.8=tout#2 58.10=mal#2 59.4=fut#2 61.2=que#6 62.4=fit#2 62.9=bien#2 62.10=voir#2')
e('la-laitiere-et-le-pot-au-lait', '1.4=tête#2 3.7=ville#3 4.3=court#2 4.9=pas#3 4.8=grands#2 5.1=ayant#2 5.2=mis#2 5.3=ce#2 9.1=tout#2 11.3=allait#2 12.3=est#3 14.4=bien#2 16.3=à#2 16.9=son#2 18.5=de#5 21.1=que#2 23.4=adieu#2 28.6=fut#2 28.7=fait#3 29.5=pot#2 30.6=campagne#2 32.4=laitière#2 33.4=que#5 34.7=est#3 36.3=bien#3 36.5=monde#3 38.9=brave#2 38.4=seul#2 43.6=devant#2')
