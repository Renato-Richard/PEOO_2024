from abc import ABC, abstractmethod
class CRUD(ABC):
  objetos = []
  @classmethod
  def create(cls, obj):
    cls.open()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.save()
  @classmethod
  def read(cls):
    cls.open()
    return cls.objetos
  @classmethod
  def read_ID(cls, id):
    cls.open()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  @classmethod
  def update(cls, obj):
    c = cls.read_ID(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.objetos.append(obj)
      cls.save()
  @classmethod
  def delete(cls, obj):
    c = cls.read_ID(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.save()
  @classmethod
  @abstractmethod
  def save(cls):
    pass
  @classmethod
  @abstractmethod
  def open(cls):
    pass