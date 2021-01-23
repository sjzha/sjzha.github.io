#! /usr/bin/env python

from crossref_commons import retrieval

doi_list_first_author = [
    "10.31635/ccschem.020.201900096",
    "10.1039/c8sc00802g",
]

doi_list_other = [
    "10.1021/acs.jpcc.7b11394",
    "10.1021/acscatal.8b00797",
    "10.1002/anie.201801463",
    "10.1126/sciadv.aar5418",
    "10.1038/s41467-018-06967-8",
    "10.1002/aic.16492",
    "10.1021/acscatal.9b00499",
    "10.1021/acscatal.8b04701",
    "10.1038/s41578-019-0152-x",
]

# style: http://api.crossref.org/styles


def get_bib(doi: str):
    j = retrieval.get_publication_as_json(doi)
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
    deposited_time = j["created"]["timestamp"]
    return deposited_time, bib


doi_bib_first_author = []
for i in doi_list_first_author:
    j = get_bib(i)
    doi_bib_first_author.append(j)

doi_bib_other = []
for i in doi_list_other:
    j = get_bib(i)
    doi_bib_other.append(j)

with open("README.md", "w") as f:
    f.write("[Email](mailto:zha@kit.edu)\n\n")
    f.write("[ORCID](https://orcid.org/0000-0001-9316-5047)\n\n")
    f.write("### Pulications (First author)\n\n")
    for i in sorted(doi_bib_first_author, reverse=True):
        f.write(i[1])
    f.write("### Pulications (Other)\n\n")
    for i in sorted(doi_bib_other, reverse=True):
        f.write(i[1])
