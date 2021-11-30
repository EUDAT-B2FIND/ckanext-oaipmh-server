from lxml.etree import SubElement
from lxml.etree import Element
from oaipmh.server import NS_XSI

NS_OAIDATACITE = 'http://schema.datacite.org/oai/oai-1.0/'
NS_EUDATCORE = 'http://schema.eudat.eu/schema/kernel-1'


def eudatcore_writer(element, metadata):
    '''Transform oaipmh.common.Metadata metadata dictionaries to lxml.etree.Element XML documents.
    '''
    e_r = SubElement(element, nseudatcore('resource'), nsmap={None: NS_EUDATCORE, 'xsi': NS_XSI})
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
            if k == 'identifiers':
                if v:
                    e_ids = SubElement(e_r, nseudatcore('identifiers'))
                    e_id = SubElement(e_ids, nseudatcore('identifier'), identifierType=v[1])
                    e_id.text = v[0]
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
                    fund_info = fund.split(',')
                    e_fund = SubElement(e_funds, nseudatcore('fundingReference'))
                    e_fund_name = SubElement(e_fund, nseudatcore('funderName'))
                    e_fund_name.text = fund_info[0]
                    if len(fund_info) > 1:
                        e_fund_awardno = SubElement(e_fund, nseudatcore('awardNumber'))
                        e_fund_awardno.text = fund_info[1]
                continue
            if k == 'spatialCoverage':
                if v:
                    e_spatial_coverages = SubElement(e_r, nseudatcore('spatialCoverages'))
                    e_spatial_coverage = SubElement(e_spatial_coverages, nseudatcore('spatialCoverage'))
                    if v[0]:
                        e_spatial_places = SubElement(e_spatial_coverage, nseudatcore('geoLocationPlace'))
                        e_spatial_places.text = v[0]
                    if v[1]:
                        values = v[1].split(',')
                        e_point = SubElement(e_spatial_coverage, nseudatcore('geoLocationPoint'))
                        e_point_long = SubElement(e_point, nseudatcore('pointLongitude'))
                        e_point_long.text = values[0]
                        e_point_lat = SubElement(e_point, nseudatcore('pointLatitude'))
                        e_point_lat.text = values[1]
                    elif v[2]:
                        values = v[2].split(',')
                        e_bbox = SubElement(e_spatial_coverage, nseudatcore('geoLocationBox'))
                        e_bbox_west = SubElement(e_bbox, nseudatcore('westBoundLongitude'))
                        e_bbox_west.text = values[0]
                        e_bbox_east = SubElement(e_bbox, nseudatcore('eastBoundLongitude'))
                        e_bbox_east.text = values[1]
                        e_bbox_south = SubElement(e_bbox, nseudatcore('southBoundLatitude'))
                        e_bbox_south.text = values[2]
                        e_bbox_north = SubElement(e_bbox, nseudatcore('northBoundLatitude'))
                        e_bbox_north.text = values[3]

                continue
            if k == 'temporalCoverage':
                if v:
                    e_temporal_coverages = SubElement(e_r, nseudatcore('temporalCoverages'))
                    if v[0] or v[1]:
                        e_temporal_coverage = SubElement(e_temporal_coverages, nseudatcore('temporalCoverage'))
                        if v[0]:
                            e_start = SubElement(e_temporal_coverage, nseudatcore('startDate'),format='ISO-8601')
                            e_start.text = v[0]
                        if v[1]:
                            e_end = SubElement(e_temporal_coverage, nseudatcore('endDate'),format='ISO-8601')
                            e_end.text = v[1]
                    if v[2]:
                        e_temporal_coverage = SubElement(e_temporal_coverages, nseudatcore('temporalCoverage'))
                        e_span = SubElement(e_temporal_coverage, nseudatcore('span'))
                        e_span.text = v[2]
                continue


def nseudatcore(name):
    return '{%s}%s' % (NS_EUDATCORE, name)


def nsoaidatacite(name):
    return '{%s}%s' % (NS_OAIDATACITE, name)
