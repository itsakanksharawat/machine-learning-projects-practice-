from langchain_community.document_loaders import WebBaseLoader
url='https://www.flipkart.com/samsung-watch-5-40mmsuper-amoled-displaybluetooth-calling-body-composition-tracking/p/itm2918bd626d66e?pid=SMWGH7W4ZMK7GTNQ&lid=LSTSMWGH7W4ZMK7GTNQKIZKZS&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_1&otracker=clp_omu_Stylish%2BSmartwatches_1_3.dealCard.OMU_electronics-republic-day-sale-dt-store_electronics-republic-day-sale-dt-store_NW0AJYD43YN8_2&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Stylish%2BSmartwatches_NA_dealCard_cc_1_NA_view-all_2&fm=neo%2Fmerchandising&iid=95d63f35-fa93-497b-9d35-0b5a5c21cd45.SMWGH7W4ZMK7GTNQ.SEARCH&ppt=browse&ppn=browse&ssid=qpon6krfrk0000001768724811486'
loader = WebBaseLoader(url)
docs = loader.load()
print(len(docs))
print(docs[0].page_content)
