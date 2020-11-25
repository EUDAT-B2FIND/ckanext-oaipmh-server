from iso639 import languages
from lxml.etree import SubElement
from lxml.etree import Element
from oaipmh.server import NS_XSI

NS_OAIDATACITE = 'http://schema.datacite.org/oai/oai-1.0/'
NS_DATACITE = 'http://schema.datacite.org/meta/kernel-4.1/'
event_to_dt = {'collection': 'Collected',
               'creation': 'Created',
               'extended': 'Updated',
               'changed': 'Updated',
               'published': 'Issued',
               'sent': 'Submitted',
               'received': 'Accepted',
               'modified': 'Updated'}


def _convert_language(lang):
    '''
    Convert alpha2 language (eg. 'en') to terminology language (eg. 'eng')
    '''
    try:
        lang_object = languages.get(part2t=lang)
        return lang_object.part1
    except KeyError as ke:
        # TODO: Parse ISO 639-2 B/T ?
        # log.debug('Invalid language: {ke}'.format(ke=ke))
        return ''


def _append_agent(e_agent_parent, role, key, value, roletype=None):
    for agent in value:
        e_agent = SubElement(e_agent_parent, nsdatacite(role))
        if roletype:
            e_agent.set(role + 'Type', roletype)
        agentname = role + 'Name'
        e_agent_name = SubElement(e_agent, nsdatacite(agentname))
        e_agent_name.text = agent['name']
        org = agent.get('organisation')
        if org:
            e_affiliation = SubElement(e_agent, nsdatacite('affiliation'))
            e_affiliation.text = org


def datacite_writer(element, metadata):
    '''Transform oaipmh.common.Metadata metadata dictionaries to lxml.etree.Element XML documents.
    '''
    e_dc = SubElement(element, nsoaidatacite('oai_datacite'),
                      nsmap = {None: NS_OAIDATACITE, 'xsi': NS_XSI})
    e_dc.set('{%s}schemaLocation' % NS_XSI, '%s http://schema.datacite.org/oai/oai-1.0/oai.xsd' % NS_OAIDATACITE)
    e_irq = SubElement(e_dc, nsoaidatacite('isReferenceQuality'))
    e_irq.text = 'false'
    e_sv = SubElement(e_dc, nsoaidatacite('schemaVersion'))
    e_sv.text = '4.1'
    e_ds = SubElement(e_dc, nsoaidatacite('datacentreSymbol'))
    e_ds.text = 'EUDAT B2FIND'
    e_pl = SubElement(e_dc, nsoaidatacite('payload'))
    e_r = SubElement(e_pl, nsdatacite('resource'), nsmap = {None: NS_DATACITE, 'xsi': NS_XSI})
    e_r.set('{%s}schemaLocation' % NS_XSI, '%s http://schema.datacite.org/meta/kernel-4.1/metadata.xsd' % NS_DATACITE)


    idType_state = None
    alt_idType_state = None

    map = metadata.getMap()
    for k, v in map.iteritems():
        if v:
            #if '/@' in k:
                #continue
            if k == 'titles':
                e_titles = SubElement(e_r, nsdatacite(k))
                e_title_primary = SubElement(e_titles, nsdatacite('title'))
                e_title_primary.text = v[0]
                continue
            if k == 'descriptions':
                e_descs = SubElement(e_r, nsdatacite(k))
                e_desc = SubElement(e_descs, nsdatacite('description'), descriptionType="Abstract")
                e_desc.text = v[0]
                continue
            if k == 'resourceType':
                e_resourceType = SubElement(e_r, nsdatacite(k), resourceTypeGeneral="Other")
                e_resourceType.text = v[0]
                continue
            if k == 'subjects':
                e_subjects = SubElement(e_r, nsdatacite(k))
                for subject in v:
                    e_subject = SubElement(e_subjects, nsdatacite('subject'))
                    e_subject.text = subject
                continue
            if k == 'creator':
                e_creators = SubElement(e_r, nsdatacite('creators'))
                for creatorName in v:
                    e_creator = SubElement(e_creators, nsdatacite(k))
                    e_creatorName = SubElement(e_creator, nsdatacite('creatorName'))
                    e_creatorName.text = creatorName
                continue
            if k == 'contributor':
                e_contributors = SubElement(e_r, nsdatacite('contributors'))
                for contributorName in v:
                    e_contributor = SubElement(e_contributors, nsdatacite(k), contributorType="Other")
                    e_contributorName = SubElement(e_contributor, nsdatacite('contributorName'))
                    e_contributorName.text = contributorName
                continue
            if k == 'publisher':
                e_publisher = SubElement(e_r, nsdatacite('publisher'))
                e_publisher.text = str(v[0])
                continue
            if k == 'language':
                e_language = SubElement(e_r, nsdatacite('language'))
                e_language.text = str(v[0])
                continue
            if k == 'format':
                e_formats = SubElement(e_r, nsdatacite('formats'))
                for format in v:
                    e_format = SubElement(e_formats, nsdatacite(k))
                    e_format.text = format
                continue
            if k == 'size':
                e_sizes = SubElement(e_r, nsdatacite('sizes'))
                for size in v:
                    e_size = SubElement(e_sizes, nsdatacite(k))
                    e_size.text = size
                continue
            if k == 'publicationYear':
                e_publicationYear = SubElement(e_r, nsdatacite('publicationYear'))
                e_publicationYear.text = str(v[0])
                continue
            if k == 'rights':
                for rights in v:
                    e_rightslist = SubElement(e_r, nsdatacite('RightsList'))
                    e_rights = SubElement(e_rightslist, nsdatacite(k), rightsURI="info:eu-repo/semantics/openAccess")
                    e_rights.text = rights
                continue
            if k == 'fundingReference':
                if v[0].get('organisation') or v[0].get('name'):
                    e_agent_parent = e_r.find(".//{*}" + 'contributors')
                    if not e_agent_parent:
                        e_agent_parent = SubElement(e_r, nsdatacite('contributors'))
                    for agent in v:
                        e_agent = SubElement(e_agent_parent, nsdatacite('contributor'))
                        e_agent.set('contributorType', 'Funder')
                        e_agent_name = SubElement(e_agent, nsdatacite('contributorName'))
                        e_agent_name.text = agent.get('organisation') or agent.get('name')
                continue
            if k == 'dates':
                e_dates = SubElement(e_r, nsdatacite(k))
                for event in v:
                    e_date = SubElement(e_dates, nsdatacite('date'))
                    e_date.text = event['when']
                    e_date.set('dateType', event_to_dt[event['type']])
                continue
            if k == 'identifier':
                if idType_state is not None:
                    e_ids = SubElement(e_r, nsdatacite('identifier'), identifierType=idType_state)
                    e_ids.text = str(v[0])
                continue
            if k == 'alternateIdentifier':
                if alt_idType_state is not None:
                    alt_ids = SubElement(e_r, nsdatacite('alternateIdentifier'), alternateIdentifierType=alt_idType_state)
                    alt_ids.text = str(v[0])
                continue
            if k == 'identifierType':
                idType_state = str(v[0])
                continue
            if k == 'alternateIdentifierType':
                alt_idType_state = str(v[0])
                continue

            # e = SubElement(e_r, nsdatacite(k))
            # e.text = v[0] if isinstance(v, list) else v

    #for k, v in map.iteritems():
        #if '/@' in k:
            #element, attr = k.split('/@')
            #print(e_r.tag)
            #e = e_r.find(".//{*}" + element, )
            #if e is not None:
                #e.set(attr, v[0] if isinstance(v, list) else v)


def nsdatacite(name):
    return '{%s}%s' % (NS_DATACITE, name)


def nsoaidatacite(name):
    return '{%s}%s' % (NS_OAIDATACITE, name)
