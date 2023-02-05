from hausdorffvertailu import m_hausdorff_etaisyys


def k_pienimmat(k, luokiteltava, harjoitusdata, harjoitusnimikkeet):
    vertailut = {}
    for kuva_indexi in range(0,harjoitusdata):
        ero = m_hausdorff_etaisyys(luokiteltava, harjoitusdata[kuva_indexi])
        vertailut[ero] = harjoitusnimikkeet[kuva_indexi]

    jarjestys = sorted(vertailut.keys(),reverse=True)
    
    maarat = {}

    for i in range(0, k):
        if maarat[vertailut[jarjestys[i]]] is False:
            maarat[vertailut[jarjestys[i]] = 1
        else:
            maarat[vertailut[jarjestys[i]]] += 1
    
    yleisin = sorted
