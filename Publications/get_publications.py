#!/usr/bin/env python
# style: http://api.crossref.org/styles
from crossref_commons import retrieval


def get_bib(doi_dict: dict) -> list:
    """This function is used to get all the detailed information via DOI.

    Args:
        doi (str): DOI number.

    Returns:
        dict: The output will look like the structure below,
            {"doi": [deposited_time, bib],}
    """
    doi_infos = []
    for doi, first_author in doi_dict.items():
        doi_info = []
        j = retrieval.get_publication_as_json(doi)
        if first_author:
            line1 = "⭐️ **{}**  \n".format(j["title"][0])
        else:
            line1 = "**{}**  \n".format(j["title"][0])
        line2 = ""
        for k in j["author"]:
            line2 = line2 + "{} {}, ".format(k["given"], k["family"])
        try:
            issue_n = j["issue"]
        except KeyError:
            issue_n = ""
        try:
            page_n = j["page"]
        except KeyError:
            page_n = ""
        line3 = "  \n{} {}, {}, {}  \n".format(
            j["short-container-title"][0],
            j["issued"]["date-parts"][0][0],
            issue_n,
            page_n,
        )
        line4 = "[DOI: {}](https://doi.org/{})\n\n".format(j["DOI"], j["DOI"])
        bib = line1 + line2[:-2] + line3 + line4
        doi_info.append(doi)
        doi_info.append(first_author)
        doi_info.append(j["created"]["timestamp"])
        doi_info.append(bib)
        doi_infos.append(doi_info)
    return sorted(doi_infos, key=lambda x: x[2], reverse=True)


# "COx Hydrogenation CoCu Catalyst"
doi_dict_project3 = {
    "10.1021/acscatal.9b00499": False,
    "10.1002/anie.202109027": False,
}

# "Reactivity Descriptor"
doi_dict_project2 = {
    "10.31635/ccschem.020.201900096": True,
    "10.1038/s41578-019-0152-x": False,
}

# "Propane Dehydrogenation PtX Catalyst"
doi_dict_project1 = {
    "10.1039/c8sc00802g": True,
    "10.1126/sciadv.aar5418": False,
    "10.1038/s41467-018-06967-8": False,
}

# "Other"
doi_dict_project0 = {
    "10.1021/acs.jpcc.7b11394": False,
    "10.1021/acscatal.8b00797": False,
    "10.1002/anie.201801463": False,
    "10.1002/aic.16492": False,
    "10.1021/acscatal.8b04701": False,
}

with open("📚Publications.md", "w") as f:
    f.write("---\n")
    f.write("layout: default\n")
    f.write("title: 📚Publications\n")
    f.write("nav_order: 2\n")
    f.write("---\n\n")
    f.write("# 📚Publications\n\n")
    f.write("## Project 3: COx Hydrogenation CoCu Catalyst\n\n")
    doi_info_3 = get_bib(doi_dict_project3)
    for i in doi_info_3:
        f.write(i[3])
    f.write("## Project 2: Reactivity Descriptor\n\n")
    doi_info_2 = get_bib(doi_dict_project2)
    for i in doi_info_2:
        f.write(i[3])
    f.write("## Project 1: Propane Dehydrogenation PtX Catalyst\n\n")
    doi_info_1 = get_bib(doi_dict_project1)
    for i in doi_info_1:
        f.write(i[3])
    f.write("## Other\n\n")
    doi_info_0 = get_bib(doi_dict_project0)
    for i in doi_info_0:
        f.write(i[3])
