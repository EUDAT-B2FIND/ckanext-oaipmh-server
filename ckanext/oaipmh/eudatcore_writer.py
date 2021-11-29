from lxml.etree import SubElement
from lxml.etree import Element
from oaipmh.server import NS_XSI

NS_OAIDATACITE = 'http://schema.datacite.org/oai/oai-1.0/'
NS_EUDATCORE = 'http://schema.eudat.eu/schema/kernel-1'


def eudatcore_writer(element, metadata):
    '''Transform oaipmh.common.Metadata metadata dictionaries to lxml.etree.Element XML documents.
    '''
    e_dc = SubElement(element, nsoaidatacite('oai_eudatcore'),
                      nsmap={None: NS_OAIDATACITE, 'xsi': NS_XSI})
    e_dc.set('{%s}schemaLocation' % NS_XSI, '%s http://schema.datacite.org/oai/oai-1.0/oai.xsd' % NS_OAIDATACITE)
    e_irq = SubElement(e_dc, nsoaidatacite('isReferenceQuality'))
    e_irq.text = 'false'
    e_sv = SubElement(e_dc, nsoaidatacite('schemaVersion'))
    e_sv.text = '2.0'
    e_ds = SubElement(e_dc, nsoaidatacite('datacentreSymbol'))
    e_ds.text = 'EUDAT B2FIND'
    e_pl = SubElement(e_dc, nsoaidatacite('payload'))
    e_r = SubElement(e_pl, nseudatcore('resource'), nsmap={None: NS_EUDATCORE, 'xsi': NS_XSI})
    e_r.set('{%s}schemaLocation' % NS_XSI, '%s https://gitlab.eudat.eu/eudat-metadata/eudat-core-schema/-/raw/master/eudat-core.xsd' % NS_EUDATCORE)

    map = metadata.getMap()
    for k, v in map.iteritems():
        if v:
            if k == 'community':
                if v:
                    e_com = SubElement(e_r, nseudatcore('community'))
                    e_com.text = v[0]
                continue
            if k == 'version':
                if v:
                    e_version = SubElement(e_r, nseudatcore('version'))
                    e_version.text = str(v[0])
                continue
            if k == 'titles':
                e_titles = SubElement(e_r, nseudatcore(k))
                e_title_primary = SubElement(e_titles, nseudatcore('title'))
                e_title_primary.text = v[0]
                continue
            if k == 'descriptions':
                e_descs = SubElement(e_r, nseudatcore(k))
                e_desc = SubElement(e_descs, nseudatcore('description'))
                e_desc.text = v[0]
                continue
            if k == 'resourceType':
                e_resourceType = SubElement(e_r, nseudatcore(k))
                e_resourceType.text = v[0]
                continue
            if k == 'keywords':
                e_keywords = SubElement(e_r, nseudatcore(k))
                for keyword in v:
                    e_keyword = SubElement(e_keywords, nseudatcore('keyword'))
                    e_keyword.text = keyword
                continue
            if k == 'disciplines':
                e_disciplines = SubElement(e_r, nseudatcore(k))
                for discipline in v:
                    e_discipline = SubElement(e_disciplines, nseudatcore('discipline'))
                    e_discipline.text = discipline
                continue
            if k == 'creator':
                e_creators = SubElement(e_r, nseudatcore('creators'))
                for creatorName in v:
                    e_creator = SubElement(e_creators, nseudatcore('creator'))
                    e_creator_name = SubElement(e_creator, nseudatcore('creatorName'))
                    e_creator_name.text = creatorName
                continue
            if k == 'contributor':
                e_contributors = SubElement(e_r, nseudatcore('contributors'))
                for contributorName in v:
                    e_contributor = SubElement(e_contributors, nseudatcore('contributor'))
                    e_contributor.text = contributorName
                continue
            if k == 'publisher':
                e_publishers = SubElement(e_r, nseudatcore('publishers'))
                for publisher in v:
                    e_publisher = SubElement(e_publishers, nseudatcore('publisher'))
                    e_publisher.text = publisher
                continue
            if k == 'contact':
                e_contacts = SubElement(e_r, nseudatcore('contacts'))
                for contact in v:
                    e_contact = SubElement(e_contacts, nseudatcore('contact'))
                    e_contact.text = contact
                continue
            if k == 'format':
                e_formats = SubElement(e_r, nseudatcore('formats'))
                for format in v:
                    e_format = SubElement(e_formats, nseudatcore('format'))
                    e_format.text = format
                continue
            if k == 'size':
                e_sizes = SubElement(e_r, nseudatcore('sizes'))
                for size in v:
                    e_size = SubElement(e_sizes, nseudatcore('size'))
                    e_size.text = size
                continue
            if k == 'rights':
                e_rightslist = SubElement(e_r, nseudatcore('rightsList'))
                for rights in v:
                    e_rights = SubElement(e_rightslist, nseudatcore(k))
                    e_rights.text = rights
                continue
            if k == 'DOI':
                if v:
                    e_doi = SubElement(e_r, nseudatcore('DOI'))
                    e_doi.text = v[0]
                continue
            if k == 'PID':
                if v:
                    e_pid = SubElement(e_r, nseudatcore('PID'))
                    e_pid.text = v[0]
                continue
            if k == 'source':
                if v:
                    e_pid = SubElement(e_r, nseudatcore('source'))
                    e_pid.text = v[0]
                continue
            if k == 'relatedIdentifier':
                e_rel_ids = SubElement(e_r, nseudatcore('relatedIdentifiers'))
                for url in v:
                    e_rel_id = SubElement(e_rel_ids, nseudatcore('relatedIdentifier'))
                    e_rel_id.text = url
                continue
            if k == 'metadataAccess':
                if v:
                    e_maccess = SubElement(e_r, nseudatcore('metadataAccess'))
                    e_maccess.text = v[0]
                continue
            if k == 'publicationYear':
                if v:
                    e_year = SubElement(e_r, nseudatcore('publicationYear'))
                    e_year.text = str(v[0])
                continue
            if k == 'openAccess':
                if v:
                    e_open_access = SubElement(e_r, nseudatcore('openAccess'))
                    e_open_access.text = str(v[0])
                continue
            if k == 'language':
                e_languages = SubElement(e_r, nseudatcore('languages'))
                for language in v:
                    e_language = SubElement(e_languages, nseudatcore('language'))
                    e_language.text = language
                continue
            if k == 'fundingReference':
                e_funds = SubElement(e_r, nseudatcore('fundingReferences'))
                for fund in v:
                    e_fund = SubElement(e_funds, nseudatcore('fundingReference'))
                    e_fund.text = fund
                continue
            if k == 'spatialCoverage':
                if v:
                    e_spatial_coverages = SubElement(e_r, nseudatcore('spatialCoverages'))
                    e_spatial_coverage = SubElement(e_spatial_coverages, nseudatcore('spatialCoverage'))
                    e_spatial_places = SubElement(e_spatial_coverage, nseudatcore('geoLocationPlace'))
                    e_spatial_places.text = v[0]
                continue
            if k == 'temporalCoverage':
                if v:
                    e_temporal_coverage = SubElement(e_r, nseudatcore('temporalCoverage'))
                    e_temporal_coverage.text = v[0]
                continue


def nseudatcore(name):
    return '{%s}%s' % (NS_EUDATCORE, name)


def nsoaidatacite(name):
    return '{%s}%s' % (NS_OAIDATACITE, name)
