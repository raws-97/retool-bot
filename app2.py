from controller import *

def app():
    # data_list = getData(uploader_name,squad)
    data_list = getData('putra',squad)

    for folder in reversed(data_list):
        createFolder(folder['listing_id'])

    driver.get(retool)
    loginFirst()
    clasificationLoop(reversed(data_list))


if __name__ == '__main__':
    app()

