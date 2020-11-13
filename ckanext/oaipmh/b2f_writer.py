from lxml.etree import SubElement
from lxml.etree import Element
from oaipmh.server import NS_XSI

NS_OAIDATACITE = 'http://schema.datacite.org/oai/oai-1.0/'
NS_B2F = 'http://b2find.eudat.eu/schema/b2f/2.0/'


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
    e_r.set('{%s}schemaLocation' % NS_XSI, '%s http://b2find.eudat.eu/schema/b2f/2.0/meta.xsd' % NS_B2F)

    map = metadata.getMap()
    for k, v in map.iteritems():
        if v:
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
                    e_discipline.text = discipline
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
            if k == 'contact':
                e_contacts = SubElement(e_r, nsb2f('contacts'))
                for contact in v:
                    e_contact = SubElement(e_contacts, nsb2f('contact'))
                    e_contact.text = contact
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
            if k == 'publicationYear':
                if v:
                    e_year = SubElement(e_r, nsb2f('publicationYear'))
                    e_year.text = str(v[0])
                continue
            if k == 'language':
                e_languages = SubElement(e_r, nsb2f('languages'))
                for language in v:
                    e_language = SubElement(e_languages, nsb2f('language'))
                    e_language.text = language
                continue
            if k == 'fundingReference':
                e_funds = SubElement(e_r, nsb2f('fundingReferences'))
                for fund in v:
                    e_fund = SubElement(e_funds, nsb2f('fundingReference'))
                    e_fund.text = fund
                continue
            if k == 'spatialCoverage':
                if v:
                    e_spatial_coverage = SubElement(e_r, nsb2f('spatialCoverage'))
                    e_spatial_coverage.text = str(v[0])
                continue
            if k == 'temporalCoverage':
                if v:
                    e_temporal_coverage = SubElement(e_r, nsb2f('temporalCoverage'))
                    e_temporal_coverage.text = str(v[0])
                continue


def nsb2f(name):
    return '{%s}%s' % (NS_B2F, name)


def nsoaidatacite(name):
    return '{%s}%s' % (NS_OAIDATACITE, name)
