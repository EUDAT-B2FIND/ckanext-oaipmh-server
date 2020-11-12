from lxml.etree import SubElement
from lxml.etree import Element
from oaipmh.server import NS_XSI

NS_OAIDATACITE = 'http://schema.datacite.org/oai/oai-1.0/'
NS_B2F = 'http://b2find.eudat.eu/schemas/'


def b2f_writer(element, metadata):
    '''Transform oaipmh.common.Metadata metadata dictionaries to lxml.etree.Element XML documents.
    '''
    e_dc = SubElement(element, nsoaidatacite('oai_b2f'),
                      nsmap={None: NS_OAIDATACITE, 'xsi': NS_XSI})
    e_dc.set('{%s}schemaLocation' % NS_XSI, '%s http://schema.datacite.org/oai/oai-1.0/oai.xsd' % NS_OAIDATACITE)
    e_irq = SubElement(e_dc, nsoaidatacite('isReferenceQuality'))
    e_irq.text = 'false'
    e_sv = SubElement(e_dc, nsoaidatacite('schemaVersion'))
    e_sv.text = '2.0'
    e_ds = SubElement(e_dc, nsoaidatacite('datacentreSymbol'))
    e_ds.text = 'EUDAT B2FIND'
    e_pl = SubElement(e_dc, nsoaidatacite('payload'))
    e_r = SubElement(e_pl, nsb2f('resource'), nsmap={None: NS_B2F, 'xsi': NS_XSI})
    e_r.set('{%s}schemaLocation' % NS_XSI, '%s http://b2find.eudat.eu/schemas/b2find_schema_2.0.xsd' % NS_B2F)

    # idType_state = None
    # alt_idType_state = None

    map = metadata.getMap()
    for k, v in map.iteritems():
        if v:
            # if '/@' in k:
            #     continue
            if k == 'titles':
                e_titles = SubElement(e_r, nsb2f(k))
                e_title_primary = SubElement(e_titles, nsb2f('title'))
                e_title_primary.text = v[0]
                continue
            if k == 'descriptions':
                e_descs = SubElement(e_r, nsb2f(k))
                e_desc = SubElement(e_descs, nsb2f('description'))
                e_desc.text = v[0]
                continue
            if k == 'resourceType':
                e_resourceType = SubElement(e_r, nsb2f(k))
                e_resourceType.text = v[0]
                continue
            if k == 'keywords':
                e_keywords = SubElement(e_r, nsb2f(k))
                for keyword in v:
                    e_keyword = SubElement(e_keywords, nsb2f('keyword'))
                    e_keyword.text = keyword
                continue
            if k == 'disciplines':
                e_disciplines = SubElement(e_r, nsb2f(k))
                for discipline in v:
                    e_discipline = SubElement(e_disciplines, nsb2f('discipline'))
                    e_discipline.text = keyword
                continue
            if k == 'creator':
                e_creators = SubElement(e_r, nsb2f('creators'))
                for creatorName in v:
                    e_creator = SubElement(e_creators, nsb2f('creator'))
                    e_creator.text = creatorName
                continue
            if k == 'contributor':
                e_contributors = SubElement(e_r, nsb2f('contributors'))
                for contributorName in v:
                    e_contributor = SubElement(e_contributors, nsb2f('contributor'))
                    e_contributor.text = contributorName
                continue
            if k == 'rights':
                e_rightslist = SubElement(e_r, nsb2f('RightsList'))
                for rights in v:
                    e_rights = SubElement(e_rightslist, nsb2f(k))
                    e_rights.text = rights
                continue
            if k == 'DOI':
                if v:
                    e_doi = SubElement(e_r, nsb2f('DOI'))
                    e_doi.text = str(v[0])
                continue
            if k == 'PID':
                if v:
                    e_pid = SubElement(e_r, nsb2f('PID'))
                    e_pid.text = str(v[0])
                continue
            if k == 'source':
                if v:
                    e_pid = SubElement(e_r, nsb2f('source'))
                    e_pid.text = str(v[0])
                continue

            # e = SubElement(e_r, nsb2f(k))
            # e.text = v[0] if isinstance(v, list) else v

    # for k, v in map.iteritems():
    #     if '/@' in k:
    #         element, attr = k.split('/@')
    #         print(e_r.tag)
    #         e = e_r.find(".//{*}" + element, )
    #         if e is not None:
    #             e.set(attr, v[0] if isinstance(v, list) else v)


def nsb2f(name):
    return '{%s}%s' % (NS_B2F, name)


def nsoaidatacite(name):
    return '{%s}%s' % (NS_OAIDATACITE, name)
