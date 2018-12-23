import requests
import json

from abc import ABCMeta, abstractmethod

class IRestService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self): raise NotImplementedError

    @abstractmethod
    def get(self, url): raise NotImplementedError

    @abstractmethod
    def post(self, url, param): raise NotImplementedError


class RestService(IRestService):
    def show(self):
        print('Hello, World 2!')

    def get(self, url):
        print('---------------RestService get method called!')
        return requests.get(url).json()

    def post(self, url, param):
        print('---------------RestService post method called!')
        return requests.post(url, param).json()

class SOAPService(IRestService):
    def show(self):
        print('Hello, World 2!')

    def get(self, url):
        print('---------------SOAPService get method called!')
        return requests.get(url).json()

    def post(self, url, param):
        print('---------------SOAPService pos method called!')
        return requests.post(url, param).json()


class ServiceManager(object):

    def __init__(self, IRestService):
        self._restService = IRestService

    def get(self, url):
       print("ServiceManager get method called!")
       return self._restService.get(url)

    def post(self, url, param):
       print("---------------ServiceManager post method called!")
       return self._restService.post(url, param)


# This call will fail with an exception
try:
    rest = RestService()
    restX = ServiceManager(rest)

    soap = SOAPService()
    soapX = ServiceManager(soap)
except Exception as exc:
    print('Failed as it should!')

#getObjRest = restX.get("https://reqres.in/api/users/2")
#print(getObjRest)


request ={"name": "morpheus","job": "leader"}
postObject = restX.post("https://reqres.in/api/users", request)
print(postObject)


#getObjSoap = soapX.get("https://reqres.in/api/users/2")
#print(getObjSoap)