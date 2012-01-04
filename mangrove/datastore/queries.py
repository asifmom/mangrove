# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from mangrove.datastore.database import DatabaseManager
from mangrove.datastore.entity import Entity
from mangrove.validate import is_string

def get_entity_count_for_type(dbm, entity_type):
    rows = dbm.view.by_short_codes(descending=True,
                                   startkey=[[entity_type], {}], endkey=[[entity_type]], group_level=1)
    return rows[0][u"value"] if len(rows) else 0

def get_entities_by_type(dbm, entity_type):
    """
    Return a list of all entities with this type.
    """
    # TODO: change this?  for now it assumes _type is
    # non-heirarchical. Might also benefit from using get_many.
    assert isinstance(dbm, DatabaseManager)
    assert is_string(entity_type)

    rows = dbm.view.by_type(key=entity_type, include_docs=True)
    return [_get_entity_from_json(dbm, row['doc']) for row in rows]

def _get_entity_from_json(dbm ,doc):
    return Entity.new_from_doc(dbm, Entity.__document_class__.wrap(doc))
