#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:57:44 2021

@author: danney
"""
import inspect
import importlib
# import selenium
from selenium import webdriver

def obtain_selenium_submodule_drivers(module):
    r = [m for m in inspect.getmembers(module) if not m[0].startswith("_")]
    r = [w for w in r if w[0].endswith("DriverManager") and w[0] != "DriverManager"]
    # r = max(r, key= lambda x:len(x[0]))
    return r

def obtain_webdriver_avail_modules():
    r = [a for a in inspect.getmembers(webdriver) if not a[0].startswith("__")]
    return r

def obtain_webdriver_platform_class(use, members=None):
    if members is None:
        members = obtain_webdriver_avail_modules()
    for member in members:
        member_name = member[0].lower()
        
        # for avail in available:
        if use.lower() == member_name.lower():
            return member
        # platform_driver = platform.split("DriverManager")[0].lower()
        
        
        # if(platform_driver == member_name):
        #     return member
    return None

# _selenium_supported_platforms = ["firefox","chrome","opera","microsoft"]
_selenium_supported_platforms = {"firefox":["firefox"],
                                 "chrome":["chrome"],
                                 "opera":["opera"],
                                 "microsoft":["edge","ie"]
                                 }
def obtain_selenium_driver():
    driver = None
    
    members = obtain_webdriver_avail_modules()
    
    driver_sucess = False

    avail_drivers = []
    for d in _selenium_supported_platforms.keys():
        try:
            mname = f"webdriver_manager.{d}"
            module = importlib.import_module(mname)
            # print(mname,module)
            r = obtain_selenium_submodule_drivers(module)
            avail_drivers.extend(r)
            # print(r)
            for driver_module in r:
                # print("Attemting", driver_module[0], "...",)
                available = _selenium_supported_platforms[d]
                
                driver_class_success = False
                for avail in available:
                    try:
                        clas = obtain_webdriver_platform_class(avail, members)
                        # print(clas,)
                        # try:
                        
                        dpath = driver_module[1]().install()
                        # except Exception as e:
                        #     print("Failed to install driver:", e)
                        args = (dpath,)
                        kwargs = {}
                        if(d=="firefox"):
                            args = ()
                            kwargs = {"executable_path":dpath}
                        driver = clas[1](*args, **kwargs)
                        driver_class_success = True
                        break
                    except:
                        pass
                if(driver_class_success):
                    driver_sucess = True
                    # print("Success!")
                    break
            if(driver_sucess):
                break
            # from webdriver_manager.chrome import ChromeDriverManager
        except:
            print("Error")
            pass
    
    if not driver_sucess:
        raise(IOError("No available driver:", avail_drivers))

    return driver

if __name__ == "__main__":
    a = obtain_selenium_driver()
    print("Selected driver", a)