class NopData:
    # Product
    sku_pid_map = {}
    products_pub_del_tbl = {}
    # Store
    stores = {}
    # Category
    categories = {}
    # Manufacturer
    manufacturers = {}
    # Product_Category_Mapping
    product_category_mappings = {}
    # Picture            
    picture_title_map = {}
    product_picture_mapping_tbl = {}
    
    def new_product():
        product = {'ProductTypeId' : 5
                   ,'ParentGroupedProductId' : 0
                   ,'VisibleIndividually' : 1
                   ,'Name' : ''
                   ,'ShortDescription' : None
                   ,'FullDescription' : None
                   ,'AdminComment' : None
                   ,'ProductTemplateId' : 0
                   ,'VendorId' : 0
                   ,'ShowOnHomepage' : 0
                   ,'MetaKeywords' : None
                   ,'MetaDescription' : None
                   ,'MetaTitle' : None
                   ,'AllowCustomerReviews' : 0
                   ,'ApprovedRatingSum' : 0
                   ,'NotApprovedRatingSum' : 0
                   ,'ApprovedTotalReviews' : 0
                   ,'NotApprovedTotalReviews' : 0
                   ,'SubjectToAcl' : 0
                   ,'LimitedToStores' : 0
                   ,'Sku' : None
                   ,'ManufacturerPartNumber' : None
                   ,'Gtin' : None
                   ,'IsGiftCard' : 0
                   ,'GiftCardTypeId' : 0
                   ,'OverriddenGiftCardAmount' : None
                   ,'RequireOtherProducts' : 0
                   ,'RequiredProductIds' : None
                   ,'AutomaticallyAddRequiredProducts' : 0
                   ,'IsDownload' : 0
                   ,'DownloadId' : 0
                   ,'UnlimitedDownloads' : 0
                   ,'MaxNumberOfDownloads' : 0
                   ,'DownloadExpirationDays' : None
                   ,'DownloadActivationTypeId' : 0
                   ,'HasSampleDownload' : 0
                   ,'SampleDownloadId' : 0
                   ,'HasUserAgreement' : 0
                   ,'UserAgreementText' : None
                   ,'IsRecurring' : 0
                   ,'RecurringCycleLength' : 0
                   ,'RecurringCyclePeriodId' : 0
                   ,'RecurringTotalCycles' : 0
                   ,'IsRental' : 0
                   ,'RentalPriceLength' : 0
                   ,'RentalPricePeriodId' : 0
                   ,'IsShipEnabled' : 1
                   ,'IsFreeShipping' : 0
                   ,'ShipSeparately' : 0
                   ,'AdditionalShippingCharge' : 0
                   ,'DeliveryDateId' : 0
                   ,'IsTaxExempt' : 0
                   ,'TaxCategoryId' : 11
                   ,'IsTelecommunicationsOrBroadcastingOrElectronicServices' : 0
                   ,'ManageInventoryMethodId' : 0
                   ,'UseMultipleWarehouses' : 0
                   ,'WarehouseId' : 0
                   ,'StockQuantity' : 0
                   ,'DisplayStockAvailability' : 0
                   ,'DisplayStockQuantity' : 0
                   ,'MinStockQuantity' : 0
                   ,'LowStockActivityId' : 0
                   ,'NotifyAdminForQuantityBelow' : 0
                   ,'BackorderModeId' : 0
                   ,'AllowBackInStockSubscriptions' : 0
                   ,'OrderMinimumQuantity' : 1
                   ,'OrderMaximumQuantity' : 999999
                   ,'AllowedQuantities' : None
                   ,'AllowAddingOnlyExistingAttributeCombinations' : 0
                   ,'DisableBuyButton' : 0
                   ,'DisableWishlistButton' : 0
                   ,'AvailableForPreOrder' : 0
                   ,'PreOrderAvailabilityStartDateTimeUtc' : None
                   ,'CallForPrice' : 0
                   ,'Price' : 0
                   ,'OldPrice' : 0
                   ,'ProductCost' : 0
                   ,'CustomerEntersPrice' : 0
                   ,'MinimumCustomerEnteredPrice' : 0
                   ,'MaximumCustomerEnteredPrice' : 0
                   ,'BasepriceEnabled' : 0
                   ,'BasepriceAmount' : 0
                   ,'BasepriceUnitId' : 0
                   ,'BasepriceBaseAmount' : 0
                   ,'BasepriceBaseUnitId' : 0
                   ,'MarkAsNew' : 1
                   ,'MarkAsNewStartDateTimeUtc' : None
                   ,'MarkAsNewEndDateTimeUtc' : None
                   ,'HasTierPrices' : 0
                   ,'HasDiscountsApplied' : 0
                   ,'Weight' : 1
                   ,'Length' : 1
                   ,'Width' : 1
                   ,'Height' : 1
                   ,'AvailableStartDateTimeUtc' : None
                   ,'AvailableEndDateTimeUtc' : None
                   ,'DisplayOrder' : 0
                   ,'Published' : 0
                   ,'Deleted' : 0
                   #,'CreatedOnUtc' : GETUTCDATE()
                   #,'UpdatedOnUtc' : GETUTCDATE()
                   ,'NotReturnable' : 0
                   ,'CartPrice' : 0
                   ,'ProductAvailabilityRangeId' : 0
                   ,'DisplayAttributeCombinationImagesOnly' : 0}

        return product