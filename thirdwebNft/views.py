from django.shortcuts import redirect, render, HttpResponse
from . import nft_collection
from thirdweb.types.nft import NFTMetadataInput 
from io import BytesIO

def listingNFT(request):
    if request.method == 'POST' and request.FILES['mint']:
        name_nft = request.POST.get('name','')
        description_nft = request.POST.get('description','')
        image_nft = request.FILES['mint'].file
        image_nft.name = request.POST.get('name','')
        prop = {}

        nft_metadata = {
            'name': name_nft,
            'description': description_nft,
            'image': image_nft,
            'properties':prop
        }
        print(nft_metadata)

        nft_collection.nft_collection.mint(NFTMetadataInput.from_json(nft_metadata))
        return redirect("success")
        
    return render(request, "listingNFT.html",{})
    
def success(request):
    return HttpResponse("successfully uploaded")

def landingPage(request):
    return render(request, "home.html")

def showroom(request):
    return render(request, "showroom.html")