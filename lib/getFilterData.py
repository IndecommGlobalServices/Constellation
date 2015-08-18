import json,os
from pages.assetpage import AssetPage
from pages.loginpage import LoginPage

cwd = os.getcwd()
os.chdir('..')
login_file_path = os.path.join(os.getcwd(), "data\json_filterAssets.json")
filterPlaceasset_filepath = os.path.join(os.getcwd(), "data\json_filterAssets.json")
filterSchoolasset_filepath = os.path.join(os.getcwd(), "data\json_filterSchoolAssets.json")
os.chdir(cwd)

def getLoginData(self):
    loginpage = LoginPage(self.driver)
    with open(login_file_path) as data_file:
        data_text = json.load(data_file)
        for each in data_text:
            usernameText = each["username"]
            passwordText = each["password"]

def getFilterData(self):
    assetpage = AssetPage(self.driver)
    with open(filterPlaceasset_filepath) as data_file:
            assetType = json.load(data_file)

            for each in assetType:
                filterText = each["Filter_name"]
                assetpage.asset_filter_based_on_place_and_school(filterText)

def getSchoolFilterData(self):
    assetpage = AssetPage(self.driver)
    with open(filterSchoolasset_filepath) as data_file:
            data_FilterSchoolAsset_text = json.load(data_file)

            for each in data_FilterSchoolAsset_text:
                filterText = each["Filter_name"]
                assetpage.asset_filter_based_on_place_and_school(filterText)
