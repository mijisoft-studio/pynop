from .core.db import Query


class NopQuery(Query):

    # Product
    GET_ALL_SKU_PID_SQL = "SELECT Sku, Id FROM Product ORDER BY Id"
    GET_ALL_PRODUCT_PUB_DEL_SQL = "SELECT Id, Sku, Published, Deleted FROM Product"
    GET_NOP_PRODUCT_BY_SKU_SQL = "SELECT * FROM Product WHERE Sku = '{sku}'"
    GET_PRODUCT_BY_ID_SQL = "SELECT * FROM Product WHERE Id = ?"
    INSERT_COLUMN_LIST_4_4 = [
        "ProductTypeId",
        "ParentGroupedProductId",
        "VisibleIndividually",
        "Name",
        "ShortDescription",
        "FullDescription",
        "AdminComment",
        "ProductTemplateId",
        "VendorId",
        "ShowOnHomepage",
        "MetaDescription",
        "MetaTitle",
        "LimitedToStores",
        "Sku",
        "ManufacturerPartNumber",
        "Gtin",
        "RequiredProductIds",
        "UnlimitedDownloads",
        "MaxNumberOfDownloads",
        "UserAgreementText",
        "IsShipEnabled",
        "IsFreeShipping",
        "TaxCategoryId",
        "StockQuantity",
        "OrderMinimumQuantity",
        "OrderMaximumQuantity",
        "AllowedQuantities",
        "DisableBuyButton",
        "CallForPrice",
        "Price",
        "OldPrice",
        "CustomerEntersPrice",
        "MinimumCustomerEnteredPrice",
        "MaximumCustomerEnteredPrice",
        "BasepriceUnitId",
        "BasepriceBaseUnitId",
        "MarkAsNew",
        "Weight",
        "Length",
        "Width",
        "Height",
        "DisplayOrder",
        "Published",
        "Deleted",
        "NotReturnable",
        "CartPrice",
        "ProductAvailabilityRangeId",
        "AllowCustomerReviews",
        "ApprovedRatingSum",
        "NotApprovedRatingSum",
        "ApprovedTotalReviews",
        "NotApprovedTotalReviews",
        "SubjectToAcl",
        "IsGiftCard",
        "GiftCardTypeId",
        "RequireOtherProducts",
        "AutomaticallyAddRequiredProducts",
        "IsDownload",
        "DownloadId",
        "DownloadActivationTypeId",
        "HasSampleDownload",
        "SampleDownloadId",
        "HasUserAgreement",
        "IsRecurring",
        "RecurringCycleLength",
        "RecurringCyclePeriodId",
        "RecurringTotalCycles",
        "IsRental",
        "RentalPriceLength",
        "RentalPricePeriodId",
        "ShipSeparately",
        "AdditionalShippingCharge",
        "DeliveryDateId",
        "IsTaxExempt",
        "IsTelecommunicationsOrBroadcastingOrElectronicServices",
        "ManageInventoryMethodId",
        "UseMultipleWarehouses",
        "WarehouseId",
        "DisplayStockAvailability",
        "DisplayStockQuantity",
        "MinStockQuantity",
        "LowStockActivityId",
        "NotifyAdminForQuantityBelow",
        "BackorderModeId",
        "AllowBackInStockSubscriptions",
        "AllowAddingOnlyExistingAttributeCombinations",
        "DisableWishlistButton",
        "AvailableForPreOrder",
        "ProductCost",
        "BasepriceEnabled",
        "BasepriceAmount",
        "BasepriceBaseAmount",
        "HasTierPrices",
        "HasDiscountsApplied"
    ]
    INSERT_COLUMN_LIST_4_8 = [
        "ProductTypeId",
        "ParentGroupedProductId",
        "VisibleIndividually",
        "Name",
        "ShortDescription",
        "FullDescription",
        "AdminComment",
        "ProductTemplateId",
        "VendorId",
        "ShowOnHomepage",
        "MetaDescription",
        "MetaTitle",
        "LimitedToStores",
        "Sku",
        "ManufacturerPartNumber",
        "Gtin",
        "RequiredProductIds",
        "UnlimitedDownloads",
        "MaxNumberOfDownloads",
        "UserAgreementText",
        "IsShipEnabled",
        "IsFreeShipping",
        "TaxCategoryId",
        "StockQuantity",
        "OrderMinimumQuantity",
        "OrderMaximumQuantity",
        "AllowedQuantities",
        "DisableBuyButton",
        "CallForPrice",
        "Price",
        "OldPrice",
        "CustomerEntersPrice",
        "MinimumCustomerEnteredPrice",
        "MaximumCustomerEnteredPrice",
        "BasepriceUnitId",
        "BasepriceBaseUnitId",
        "MarkAsNew",
        "Weight",
        "Length",
        "Width",
        "Height",
        "DisplayOrder",
        "Published",
        "Deleted",
        "NotReturnable",
        "CartPrice",
        "ProductAvailabilityRangeId",
        "AllowCustomerReviews",
        "ApprovedRatingSum",
        "NotApprovedRatingSum",
        "ApprovedTotalReviews",
        "NotApprovedTotalReviews",
        "SubjectToAcl",
        "IsGiftCard",
        "GiftCardTypeId",
        "RequireOtherProducts",
        "AutomaticallyAddRequiredProducts",
        "IsDownload",
        "DownloadId",
        "DownloadActivationTypeId",
        "HasSampleDownload",
        "SampleDownloadId",
        "HasUserAgreement",
        "IsRecurring",
        "RecurringCycleLength",
        "RecurringCyclePeriodId",
        "RecurringTotalCycles",
        "IsRental",
        "RentalPriceLength",
        "RentalPricePeriodId",
        "ShipSeparately",
        "AdditionalShippingCharge",
        "DeliveryDateId",
        "IsTaxExempt",
        "ManageInventoryMethodId",
        "UseMultipleWarehouses",
        "WarehouseId",
        "DisplayStockAvailability",
        "DisplayStockQuantity",
        "MinStockQuantity",
        "LowStockActivityId",
        "NotifyAdminForQuantityBelow",
        "BackorderModeId",
        "AllowBackInStockSubscriptions",
        "AllowAddingOnlyExistingAttributeCombinations",
        "DisableWishlistButton",
        "AvailableForPreOrder",
        "ProductCost",
        "BasepriceEnabled",
        "BasepriceAmount",
        "BasepriceBaseAmount",
        "DisplayAttributeCombinationImagesOnly"
    ]
    
    UPDATE_COLUMN_LIST_4_4 = [
        "Name",
        "ShortDescription",
        "FullDescription",
        "LimitedToStores",
        "Sku",
        "Gtin",
        "IsShipEnabled",
        "IsFreeShipping",
        "TaxCategoryId",
        "StockQuantity",
        "OrderMinimumQuantity",
        "OrderMaximumQuantity",
        "AllowedQuantities",
        "DisableBuyButton",
        "CallForPrice",
        "Price",
        "OldPrice",
        "Weight",
        "Length",
        "Width",
        "Height",
        "DisplayOrder",
        "Published",
        "Deleted",
        "NotReturnable",
        "CartPrice",
        "Id"
    ]
    UPDATE_COLUMN_LIST_4_8 = [
        "Name",
        "ShortDescription",
        "FullDescription",
        "LimitedToStores",
        "Sku",
        "Gtin",
        "IsShipEnabled",
        "IsFreeShipping",
        "TaxCategoryId",
        "StockQuantity",
        "OrderMinimumQuantity",
        "OrderMaximumQuantity",
        "AllowedQuantities",
        "DisableBuyButton",
        "CallForPrice",
        "Price",
        "OldPrice",
        "Weight",
        "Length",
        "Width",
        "Height",
        "DisplayOrder",
        "Published",
        "Deleted",
        "NotReturnable",
        "CartPrice",
        "Id"
    ]
    # HasTierPrices,, HasDiscountsApplied, IsTelecommunicationsOrBroadcastingOrElectronicServices
    INSERT_PRODUCT_SQL_4_4 = """    
        INSERT INTO Product (
            ProductTypeId,
            ParentGroupedProductId,
            VisibleIndividually,
            Name,
            ShortDescription,
            FullDescription,
            AdminComment,
            ProductTemplateId,
            VendorId,
            ShowOnHomepage,
            MetaDescription,
            MetaTitle,
            LimitedToStores,
            Sku,
            ManufacturerPartNumber,
            Gtin,
            RequiredProductIds,
            UnlimitedDownloads,
            MaxNumberOfDownloads,
            UserAgreementText,
            IsShipEnabled,
            IsFreeShipping,
            TaxCategoryId,
            StockQuantity,
            OrderMinimumQuantity,
            OrderMaximumQuantity,
            AllowedQuantities,
            DisableBuyButton,
            CallForPrice,
            Price,
            OldPrice,
            CustomerEntersPrice,
            MinimumCustomerEnteredPrice,
            MaximumCustomerEnteredPrice,
            BasepriceUnitId,
            BasepriceBaseUnitId,
            MarkAsNew,
            Weight,
            Length,
            Width,
            Height,
            DisplayOrder,
            Published,
            Deleted,
            NotReturnable,
            CartPrice,
            ProductAvailabilityRangeId,
            AllowCustomerReviews,
            ApprovedRatingSum,
            NotApprovedRatingSum,
            ApprovedTotalReviews,
            NotApprovedTotalReviews,
            SubjectToAcl,
            IsGiftCard,
            GiftCardTypeId,
            RequireOtherProducts,
            AutomaticallyAddRequiredProducts,
            IsDownload,
            DownloadId,
            DownloadActivationTypeId,
            HasSampleDownload,
            SampleDownloadId,
            HasUserAgreement,
            IsRecurring,
            RecurringCycleLength,
            RecurringCyclePeriodId,
            RecurringTotalCycles,
            IsRental,
            RentalPriceLength,
            RentalPricePeriodId,
            ShipSeparately,
            AdditionalShippingCharge,
            DeliveryDateId,
            IsTaxExempt,
            IsTelecommunicationsOrBroadcastingOrElectronicServices,
            ManageInventoryMethodId,
            UseMultipleWarehouses,
            WarehouseId,
            DisplayStockAvailability,
            DisplayStockQuantity,
            MinStockQuantity,
            LowStockActivityId,
            NotifyAdminForQuantityBelow,
            BackorderModeId,
            AllowBackInStockSubscriptions,
            AllowAddingOnlyExistingAttributeCombinations,
            DisableWishlistButton,
            AvailableForPreOrder,
            ProductCost,
            BasepriceEnabled,
            BasepriceAmount,
            BasepriceBaseAmount,
            HasTierPrices,
            HasDiscountsApplied,
            CreatedOnUtc,
            UpdatedOnUtc
        )
        OUTPUT INSERTED.*
        VALUES (
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,
            GETUTCDATE(), GETUTCDATE()
        )
    """
    INSERT_PRODUCT_SQL_4_8 = """    
        INSERT INTO Product (
            ProductTypeId,
            ParentGroupedProductId,
            VisibleIndividually,
            Name,
            ShortDescription,
            FullDescription,
            AdminComment,
            ProductTemplateId,
            VendorId,
            ShowOnHomepage,
            MetaDescription,
            MetaTitle,
            LimitedToStores,
            Sku,
            ManufacturerPartNumber,
            Gtin,
            RequiredProductIds,
            UnlimitedDownloads,
            MaxNumberOfDownloads,
            UserAgreementText,
            IsShipEnabled,
            IsFreeShipping,
            TaxCategoryId,
            StockQuantity,
            OrderMinimumQuantity,
            OrderMaximumQuantity,
            AllowedQuantities,
            DisableBuyButton,
            CallForPrice,
            Price,
            OldPrice,
            CustomerEntersPrice,
            MinimumCustomerEnteredPrice,
            MaximumCustomerEnteredPrice,
            BasepriceUnitId,
            BasepriceBaseUnitId,
            MarkAsNew,
            Weight,
            Length,
            Width,
            Height,
            DisplayOrder,
            Published,
            Deleted,
            NotReturnable,
            CartPrice,
            ProductAvailabilityRangeId,
            AllowCustomerReviews,
            ApprovedRatingSum,
            NotApprovedRatingSum,
            ApprovedTotalReviews,
            NotApprovedTotalReviews,
            SubjectToAcl,
            IsGiftCard,
            GiftCardTypeId,
            RequireOtherProducts,
            AutomaticallyAddRequiredProducts,
            IsDownload,
            DownloadId,
            DownloadActivationTypeId,
            HasSampleDownload,
            SampleDownloadId,
            HasUserAgreement,
            IsRecurring,
            RecurringCycleLength,
            RecurringCyclePeriodId,
            RecurringTotalCycles,
            IsRental,
            RentalPriceLength,
            RentalPricePeriodId,
            ShipSeparately,
            AdditionalShippingCharge,
            DeliveryDateId,
            IsTaxExempt,
            ManageInventoryMethodId,
            UseMultipleWarehouses,
            WarehouseId,
            DisplayStockAvailability,
            DisplayStockQuantity,
            MinStockQuantity,
            LowStockActivityId,
            NotifyAdminForQuantityBelow,
            BackorderModeId,
            AllowBackInStockSubscriptions,
            AllowAddingOnlyExistingAttributeCombinations,
            DisableWishlistButton,
            AvailableForPreOrder,
            ProductCost,
            BasepriceEnabled,
            BasepriceAmount,
            BasepriceBaseAmount,
            DisplayAttributeCombinationImagesOnly,
            CreatedOnUtc,
            UpdatedOnUtc
        )
        OUTPUT INSERTED.*
        VALUES (
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,
            GETUTCDATE(), GETUTCDATE()
        )
    """
    
    UPDATE_PRODUCT_SQL_4_4 = """
    UPDATE Product
    SET     Name = ?,
            ShortDescription = ?,
            FullDescription = ?,
            LimitedToStores = ?,
            Sku = ?,
            Gtin = ?,
            IsShipEnabled = ?,
            IsFreeShipping = ?,
            TaxCategoryId = ?,
            StockQuantity = ?,
            OrderMinimumQuantity = ?,
            OrderMaximumQuantity = ?,
            AllowedQuantities = ?,
            DisableBuyButton = ?,
            CallForPrice = ?,
            Price = ?,
            OldPrice = ?,
            Weight = ?,
            Length = ?,
            Width = ?,
            Height = ?,
            DisplayOrder = ?,
            Published = ?,
            Deleted = ?,
            UpdatedOnUtc = GETUTCDATE(),
            NotReturnable = ?,
            CartPrice = ?
            WHERE Id = ?
    """
    UPDATE_PRODUCT_SQL_4_8 = """
    UPDATE Product
    SET     Name = ?,
            ShortDescription = ?,
            FullDescription = ?,
            LimitedToStores = ?,
            Sku = ?,
            Gtin = ?,
            IsShipEnabled = ?,
            IsFreeShipping = ?,
            TaxCategoryId = ?,
            StockQuantity = ?,
            OrderMinimumQuantity = ?,
            OrderMaximumQuantity = ?,
            AllowedQuantities = ?,
            DisableBuyButton = ?,
            CallForPrice = ?,
            Price = ?,
            OldPrice = ?,
            Weight = ?,
            Length = ?,
            Width = ?,
            Height = ?,
            DisplayOrder = ?,
            Published = ?,
            Deleted = ?,
            UpdatedOnUtc = GETUTCDATE(),
            NotReturnable = ?,
            CartPrice = ?
            WHERE Id = ?
    """

    # UrlRecord
    DELETE_SLUG_SQL = """
        DELETE FROM UrlRecord
        WHERE EntityId = ?
            AND EntityName = ?
    """
    INSERT_SLUG_SQL = """
        INSERT INTO UrlRecord
            (
                EntityId,
                EntityName,
                Slug,
                IsActive,
                LanguageId
            )
        OUTPUT INSERTED.*
        VALUES
            (
                ?
                ,?
                ,?
                ,?
                ,?
            )
    """
    GET_SLUG_SQL = """
        SELECT Id
            ,EntityId
            ,EntityName
            ,Slug
            ,IsActive
            ,LanguageId
        FROM UrlRecord
        WHERE EntityId = ?
        AND EntityName = ?
        AND IsActive = 1
        AND LanguageId = ?
    """
    UPDATE_SLUG_SQL = """
        UPDATE UrlRecord
        SET Slug = ?
        WHERE Id = ?
    """

    # Store
    GET_STORE_BY_NAME_SQL = """
        SELECT Id
            ,Name
            ,Url
            ,SslEnabled
            ,Hosts
            ,DefaultLanguageId
            ,DisplayOrder
            ,CompanyName
            ,CompanyAddress
            ,CompanyPhoneNumber
            ,CompanyVat
    FROM Store
    WHERE Name = ?
    """

    # Manufacturer
    GET_ALL_MANUFACTURER_SQL = """
        SELECT Id
        ,Name
        ,Description
        ,ManufacturerTemplateId
        ,MetaKeywords
        ,MetaDescription
        ,MetaTitle
        ,PictureId
        ,PageSize
        ,AllowCustomersToSelectPageSize
        ,PageSizeOptions
        ,SubjectToAcl
        ,LimitedToStores

        ,Published
        ,Deleted
        ,DisplayOrder
        ,CreatedOnUtc
        ,UpdatedOnUtc
    FROM Manufacturer
    """
    INSERT_MANUFACTURER_SQL = """
        INSERT INTO Manufacturer 
            (
                Name
                ,PageSizeOptions
                ,PageSize
                ,Published
                ,AllowCustomersToSelectPageSize
                ,LimitedToStores            
                ,CreatedOnUtc
                ,UpdatedOnUtc
                ,Deleted
                ,DisplayOrder            
                ,ManufacturerTemplateId
                ,PictureId
                ,SubjectToAcl 
                ,PriceRangeFiltering
                ,PriceFrom
                ,PriceTo
                ,ManuallyPriceRange
            )
        OUTPUT INSERTED.*
        VALUES 
            (
                ?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,GETUTCDATE()
                ,GETUTCDATE()
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
            )
    """    
    # Product_Manufacturer_Mapping
    GET_PRODUCT_MANUFACTURER_MAPPING_SQL = """
        SELECT * FROM Product_Manufacturer_Mapping pm
            LEFT JOIN Manufacturer m ON pm.ManufacturerId = m.Id
        WHERE pm.ProductId = ?
            AND pm.ManufacturerId = ?
        ORDER BY pm.DisplayOrder, pm.Id
    """
    GET_PRODUCT_MANUFACTURER_MAPPING_BY_ID_SQL = """
        SELECT Id
            ,ProductId
            ,ManufacturerId
            ,IsFeaturedProduct
            ,DisplayOrder
        FROM Product_Manufacturer_Mapping
        WHERE ProductId = ?
    """
    GET_PRODUCT_IS_CALL_ONLY_SQL = """
        SELECT * FROM Product_Manufacturer_Mapping pm
            LEFT JOIN Manufacturer m ON pm.ManufacturerId = m.Id
        WHERE pm.ProductId = ?
            AND m.Deleted <> 0
            AND m.Published = 1
            AND (LOWER(m.Name) = 'asko' OR LOWER(m.Name) = 'subzero' OR LOWER(m.Name) = 'wolf')
        ORDER BY pm.DisplayOrder, pm.Id
    """
    INSERT_PRODUCT_MANUFACTURER_MAPPING_SQL = """
        INSERT INTO Product_Manufacturer_Mapping
        (
            ProductId
            ,ManufacturerId
            ,IsFeaturedProduct
            ,DisplayOrder
        )
        OUTPUT INSERTED.*
        VALUES 
        (
            @ProductId
            ,@ManufacturerId
            ,@IsFeaturedProduct
            ,@DisplayOrder
        )
    """
    DELETE_PRODUCT_MANUFACTURER_MAPPING_SQL = """
        DELETE FROM Product_Manufacturer_Mapping WHERE ProductId = ? AND ManufacturerId != ?;
    """
    SAVE_PRODUCT_MANUFACTURER_MAPPING_SQL = """
        DECLARE @ProductId int, @ManufacturerId int, @IsFeaturedProduct bit, @DisplayOrder int;

        SET @ProductId = ?;  
        SET @ManufacturerId = ?;
        SET @IsFeaturedProduct = ?;  
        SET @DisplayOrder = ?;
        
        IF EXISTS ( SELECT 1 FROM Product_Manufacturer_Mapping pm
                        LEFT JOIN Manufacturer m ON pm.ManufacturerId = m.Id
                    WHERE pm.ProductId = @ProductId AND pm.ManufacturerId = @ManufacturerId
                    )
            BEGIN                
                SELECT * FROM Product_Manufacturer_Mapping pm
                    LEFT JOIN Manufacturer m ON pm.ManufacturerId = m.Id
                WHERE pm.ProductId = @ProductId AND pm.ManufacturerId = @ManufacturerId
            END
        ELSE
            BEGIN                
                INSERT INTO Product_Manufacturer_Mapping
                (
                    ProductId
                    ,ManufacturerId
                    ,IsFeaturedProduct
                    ,DisplayOrder
                )
                OUTPUT INSERTED.*
                VALUES 
                (
                    @ProductId
                    ,@ManufacturerId
                    ,@IsFeaturedProduct
                    ,@DisplayOrder
                )
            END
    """

    # ProductAttribute
    GET_PRODUCT_ATTRIBUTE_BY_NAME_SQL = """
        SELECT Id
            ,Name
            ,Description
        FROM ProductAttribute
        WHERE Name = ?
    """
    INSERT_PRODUCT_ATTRIBUTE_SQL = """
        INSERT INTO ProductAttribute ( Name, Description )
        OUTPUT INSERTED.*
        VALUES ( ?, ? )
    """
    DELETE_PRODUCT_ATTRIBUTE_SQL = """
        DELETE FROM ProductAttribute
        WHERE Id = ?
    """
    # PredefinedProductAttributeValue
    GET_PREDEFINED_PRODUCT_ATTRIBUTE_VALUE_SQL = """
        SELECT Id
            ,ProductAttributeId
            ,Name
            ,PriceAdjustment
            ,WeightAdjustment
            ,Cost
            ,IsPreSelected
            ,DisplayOrder
            ,PriceAdjustmentUsePercentage
        FROM PredefinedProductAttributeValue
        WHERE ProductAttributeId = ?
    """
    INSERT_PREDEFINED_PRODUCT_ATTRIBUTE_VALUE_SQL = """
        INSERT INTO PredefinedProductAttributeValue ( 
            ProductAttributeId
            ,Name
            ,PriceAdjustment
            ,WeightAdjustment
            ,Cost
            ,IsPreSelected
            ,DisplayOrder
            ,PriceAdjustmentUsePercentage
        )
        OUTPUT INSERTED.*
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ? )
    """
    UPDATE_PREDEFINED_PRODUCT_ATTRIBUTE_VALUE_PRICE_SQL = """
        UPDATE PredefinedProductAttributeValue
        SET PriceAdjustment = ?
        WHERE Id = ?
    """
    # Product_ProductAttribute_Mapping
    GET_PRODUCT_ATTRIBUTE_MAPPING_LIST_SQL = """
        SELECT DISTINCT ProductId
        FROM Product_ProductAttribute_Mapping
        WHERE ProductAttributeId = ?
    """
    GET_PRODUCT_ATTRIBUTE_MAPPING_SQL = """
        SELECT 
            Id
            ,ProductId
            ,ProductAttributeId
            ,TextPrompt
            ,IsRequired
            ,AttributeControlTypeId
            ,DisplayOrder
            ,ValidationMinLength
            ,ValidationMaxLength
            ,ValidationFileAllowedExtensions
            ,ValidationFileMaximumSize
            ,DefaultValue
            ,ConditionAttributeXml
        FROM Product_ProductAttribute_Mapping
        WHERE ProductId = ?
        AND ProductAttributeId = ?
    """
    DELETE_PRODUCT_ATTRIBUTE_MAPPING_SQL = """
        DELETE FROM Product_ProductAttribute_Mapping
        OUTPUT DELETED.*
        WHERE ProductId = ?
        AND ProductAttributeId = ?
    """
    DELETE_PRODUCT_ATTRIBUTE_MAPPING_BY_PAID_SQL = """
        DELETE FROM Product_ProductAttribute_Mapping
        WHERE ProductAttributeId = ?
    """
    INSERT_PRODUCT_ATTRIBUTE_MAPPING_SQL = """
        INSERT INTO Product_ProductAttribute_Mapping
            (   
                ProductId
                ,ProductAttributeId
                ,TextPrompt
                ,IsRequired
                ,AttributeControlTypeId
                ,DisplayOrder
                ,ValidationMinLength
                ,ValidationMaxLength
                ,ValidationFileAllowedExtensions
                ,ValidationFileMaximumSize
                ,DefaultValue
                ,ConditionAttributeXml
            )
        OUTPUT INSERTED.*
        VALUES 
            (
                ?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
            )
    """
    # ProductAttributeValue
    GET_PRODUCT_ATTRIBUTE_VALUE_SQL = """
        SELECT Id
            ,ProductAttributeMappingId
            ,AttributeValueTypeId
            ,AssociatedProductId
            ,Name
            ,ColorSquaresRgb
            ,PriceAdjustment
            ,WeightAdjustment
            ,Cost
            ,Quantity
            ,IsPreSelected
            ,DisplayOrder
            ,PictureId
            ,ImageSquaresPictureId
            ,CustomerEntersQty
            ,PriceAdjustmentUsePercentage
        FROM ProductAttributeValue
        WHERE ProductAttributeMappingId = ?
    """
    GET_PRODUCT_ATTRIBUTE_VALUE_BY_NAME_SQL = """
        SELECT Id
            ,ProductAttributeMappingId
            ,AttributeValueTypeId
            ,AssociatedProductId
            ,Name
            ,ColorSquaresRgb
            ,PriceAdjustment
            ,WeightAdjustment
            ,Cost
            ,Quantity
            ,IsPreSelected
            ,DisplayOrder
            ,PictureId
            ,ImageSquaresPictureId
            ,CustomerEntersQty
            ,PriceAdjustmentUsePercentage
        FROM ProductAttributeValue
        WHERE ProductAttributeMappingId = ?
        AND Name = ?
    """
    UPDATE_PRODUCT_ATTRIBUTE_VALUE_SQL = """
        UPDATE ProductAttributeValue
        SET  AttributeValueTypeId = ?
            ,AssociatedProductId = ?
            ,Name = ?
            ,ColorSquaresRgb = ?
            ,PriceAdjustment = ?
            ,WeightAdjustment = ?
            ,Cost = ?
            ,Quantity = ?
            ,IsPreSelected = ?
            ,DisplayOrder = ?
            ,PictureId = ?
            ,ImageSquaresPictureId = ?
            ,CustomerEntersQty = ?
            ,PriceAdjustmentUsePercentage = ?
        WHERE Id = ?
    """
    INSERT_PRODUCT_ATTRIBUTE_VALUE_SQL = """
        INSERT INTO ProductAttributeValue
            (
                ProductAttributeMappingId
                ,AttributeValueTypeId
                ,AssociatedProductId
                ,Name
                ,ColorSquaresRgb
                ,PriceAdjustment
                ,WeightAdjustment
                ,Cost
                ,Quantity
                ,IsPreSelected
                ,DisplayOrder
                ,PictureId
                ,ImageSquaresPictureId
                ,CustomerEntersQty
                ,PriceAdjustmentUsePercentage
            )
            VALUES
            (
                    ?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?
            )
    """
    DELETE_PRODUCT_ATTRIBUTE_VALUE_BY_MAPPING_SQL = """
        DELETE FROM ProductAttributeValue
        WHERE ProductAttributeMappingId = ?
    """

    # StoreMapping
    GET_STORE_MAPPING_SQL = """
        SELECT Id
            ,EntityId
            ,EntityName
            ,StoreId
        FROM StoreMapping
        WHERE EntityId = ?
        AND EntityName = ?
        AND StoreId = ?
    """
    GET_STORE_MAPPINGS_BY_ENTITY_NAME_SQL = """
        SELECT Id
            ,EntityId
            ,EntityName
            ,StoreId
        FROM StoreMapping
        WHERE EntityName = ?
    """
    GET_STORE_MAPPINGS_BY_ENTITY_ID_SQL = """
        SELECT Id
            ,EntityId
            ,EntityName
            ,StoreId
        FROM StoreMapping
        WHERE EntityName = ?
            AND EntityId = ?
    """
    INSERT_STORE_MAPPING_SQL = """
        INSERT INTO StoreMapping (EntityId, EntityName, StoreId)
        OUTPUT INSERTED.*
        VALUES (?, ?, ?)
    """
    DELETE_STORE_MAPPING_SQL = """
        DELETE FROM StoreMapping 
        WHERE StoreId = ?
        AND EntityName = ? 
        AND EntityId = ?
    """
    DELETE_STORE_MAPPING_BY_ID_SQL = """
        DELETE FROM StoreMapping 
        WHERE Id = ?
    """

    # GenericAttribute
    GET_GENERIC_ATTRIBUTE_SQL = """
        SELECT Id
            ,EntityId
            ,KeyGroup
            ,[Key]
            ,Value
            ,StoreId
            ,CreatedOrUpdatedDateUTC
        FROM GenericAttribute
        WHERE EntityId = ? AND KeyGroup = ? AND [Key] = ? AND StoreId = ?
    """
    GET_GENERIC_ATTRIBUTE_LIST_SQL = """
        SELECT Id
            ,EntityId
        FROM GenericAttribute
        WHERE KeyGroup = ? AND [Key] LIKE ? AND StoreId = ?
    """
    INSERT_GENERIC_ATTRIBUTE_SQL = """
        INSERT INTO GenericAttribute (EntityId, KeyGroup, [Key], Value, StoreId
                                    ,CreatedOrUpdatedDateUTC )
        OUTPUT INSERTED.* 
        VALUES (?, ?, ?, ?, ?, GETUTCDATE())
    """
    UPDATE_GENERIC_ATTRIBUTE_SQL = """
        UPDATE GenericAttribute
        SET Value = ?
            ,CreatedOrUpdatedDateUTC = GETUTCDATE()    
        WHERE Id = ?
    """
    DELETE_GENERIC_ATTRIBUTE_SQL = """
        DELETE FROM GenericAttribute
        WHERE EntityId = ?
        AND KeyGroup = ?
        AND [Key] = ?
    """
    DELETE_GENERIC_ATTRIBUTE_BY_ID_SQL = """
        DELETE FROM GenericAttribute
        WHERE Id = ?
    """


    # Category
    GET_ALL_CATEGORY_SQL = """
        SELECT Id
            ,Name
            ,Description
            ,CategoryTemplateId
            ,ParentCategoryId
            ,PictureId
            ,ShowOnHomepage
            ,SubjectToAcl
            ,LimitedToStores
            ,Published
            ,Deleted
            ,DisplayOrder
            ,CreatedOnUtc
            ,UpdatedOnUtc
        FROM Category
        ORDER BY ParentCategoryId, DisplayOrder, Id
    """
    GET_CATEGORY_BY_NAME_SQL = """
        SELECT Id
            ,Name
            ,Description
            ,CategoryTemplateId
            ,MetaKeywords
            ,MetaDescription
            ,MetaTitle
            ,ParentCategoryId
            ,PictureId
            ,PageSize
            ,AllowCustomersToSelectPageSize
            ,PageSizeOptions
            ,PriceRanges
            ,ShowOnHomepage
            ,IncludeInTopMenu
            ,SubjectToAcl
            ,LimitedToStores
            ,Published
            ,Deleted
            ,DisplayOrder
            ,CreatedOnUtc
            ,UpdatedOnUtc
        FROM Category
        WHERE Name = ?
    """
    GET_CATEGORY_BY_ID_SQL = """
        SELECT Id
            ,Name
            ,Description
            ,CategoryTemplateId
            ,MetaKeywords
            ,MetaDescription
            ,MetaTitle
            ,ParentCategoryId
            ,PictureId
            ,PageSize
            ,AllowCustomersToSelectPageSize
            ,PageSizeOptions
            ,PriceRanges
            ,ShowOnHomepage
            ,IncludeInTopMenu
            ,SubjectToAcl
            ,LimitedToStores
            ,Published
            ,Deleted
            ,DisplayOrder
            ,CreatedOnUtc
            ,UpdatedOnUtc
        FROM Category
        WHERE Id = ?
    """
    # Product_Category_Mapping
    GET_ALL_PRODUCT_CATEGORY_MAPPING_SQL = """
        SELECT Id,
            ProductId, 
            CategoryId, 
            IsFeaturedProduct,
            DisplayOrder 
        FROM Product_Category_Mapping
    """
    INSERT_PRODUCT_CATEGORY_MAPPING_SQL = """
        INSERT INTO Product_Category_Mapping
            (
                ProductId,
                CategoryId,
                IsFeaturedProduct,
                DisplayOrder
            )
        OUTPUT INSERTED.*
        VALUES
            (   ?, ?, ?, ? )
    """
    UPDATE_PRODUCT_CATEGORY_MAPPING_SQL = """
        UPDATE Product_Category_Mapping
        SET ProductId = ?
            ,CategoryId = ?
            ,IsFeaturedProduct = ?
            ,DisplayOrder = ?
        WHERE Id = ?
    """
    DELETE_PRODUCT_CATEGORY_MAPPING_BY_PID_SQL = """
        DELETE FROM Product_Category_Mapping    
        WHERE ProductId = ?
    """
    DELETE_PRODUCT_CATEGORY_MAPPING_SQL = """
        DELETE FROM Product_Category_Mapping    
        WHERE Id = ?
    """

    # Picture
    GET_ALL_PICTURE_SQL = """
        SELECT Id
            ,TitleAttribute
        FROM Picture
        WHERE TitleAttribute IS NOT NULL
    """
    GET_PICTURE_BY_ID_SQL = """
        SELECT * FROM Picture WHERE Id = ?
    """    
    GET_PICTURE_BY_TITLEATTRIBUTE_SQL = """
        SELECT * FROM Picture WHERE TitleAttribute=?
    """
    GET_SPECIAL_PROMO_PICTURE_BY_TITLEATTRIBUTE_SQL = """
        SELECT Id, TitleAttribute FROM Picture WHERE TitleAttribute LIKE ?
    """
    INSERT_PICTURE_SQL = """
        INSERT INTO Picture(
            MimeType            
            ,TitleAttribute
            ,SeoFilename
            ,AltAttribute
            ,IsNew
            ,VirtualPath)
        OUTPUT INSERTED.*
        VALUES (?, ?, ?, ?, ?, ?)
    """
    UPDATE_PICTURE_MIME_TYPE_SQL = """
        UPDATE Picture SET MimeType = ?, IsNew = 0 WHERE Id = ?
    """
    UPDATE_PICTURE_TITLE_ATTRIBUTE_SQL = """
        UPDATE Picture SET TitleAttribute = ?, IsNew = 0 WHERE Id = ?
    """
    UPDATE_PICTURE_SEO_SQL = """
        UPDATE Picture SET TitleAttribute = ? WHERE Id = ?
    """
    DELETE_PICTURE_SQL = """
        DELETE FROM Picture WHERE Id = ?
    """
    # Product_Picture_Mapping
    GET_ALL_PRODUCT_PICTURE_MAPPING_SQL = """
        SELECT Id, ProductId, PictureId, DisplayOrder 
        FROM Product_Picture_Mapping
        ORDER BY ProductId, DisplayOrder
    """
    GET_PRODUCT_PICTURE_MAPPING_BY_PID_SQL = """
        SELECT Id, ProductId, PictureId, DisplayOrder
        FROM Product_Picture_Mapping
        WHERE ProductId = ?
        ORDER BY DisplayOrder
    """
    GET_PRODUCT_PICTURE_MAPPING_ID_SQL = """
        SELECT Id 
        FROM Product_Picture_Mapping 
        WHERE ProductId=? AND PictureId=?
    """
    GET_PRODUCT_PICTURE_MAPPING_BY_ID_SQL = """
        SELECT *
        FROM Product_Picture_Mapping 
        WHERE Id = ?
    """
    GET_PRODUCT_PICTURE_MAPPING_BY_SKU_SQL = """
        SELECT Id, ProductId, PictureId, DisplayOrder 
        FROM Product_Picture_Mapping ppm 
        WHERE ProductId = (SELECT Id FROM Product WHERE Sku = ?)
    """
    INSERT_PRODUCT_PICTURE_MAPPING_SQL = """
        INSERT INTO Product_Picture_Mapping (ProductId, PictureId, DisplayOrder) 
        OUTPUT INSERTED.* 
        VALUES (?,?,?)
    """
    UPDATE_PRODUCT_PICTURE_MAPPING_DISPLAY_ORDER_SQL = """
        UPDATE Product_Picture_Mapping
        SET DisplayOrder = ?
        WHERE Id = ?
    """
    DELETE_PRODUCT_PICTURE_MAPPING_SQL = """
        DELETE FROM Product_Picture_Mapping 
        OUTPUT DELETED.* 
        WHERE ProductId = ? AND PictureId = ?
    """
    DELETE_PRODUCT_PICTURE_MAPPING_BY_PICID_SQL = """
        DELETE FROM Product_Picture_Mapping
        WHERE PictureId = ?
    """
    DELETE_PRODUCT_PICTURE_MAPPING_BY_PID_SQL = """
        DELETE FROM Product_Picture_Mapping
        WHERE ProductId = ?
    """
    DELETE_PRODUCT_PICTURE_MAPPING_BY_ID_SQL = """
        DELETE FROM Product_Picture_Mapping WHERE Id = ?
    """
    UPDATE_PIC_ID_IN_PRODUCT_PICTURE_MAPPING_SQL = """
        UPDATE Product_Picture_Mapping 
        SET PictureId = ? 
        WHERE PictureId = ?
    """
    # PictureEtag
    GET_PICTURE_ETAG_SQL = """
        SELECT Etag FROM PictureEtag WHERE PictureId = ?
    """
    INSERT_PICTURE_ETAG_SQL = """
        INSERT INTO PictureEtag(PictureId, Etag)
        VALUES (?, ?)
    """
    UPDATE_PICTURE_ETAG_SQL = """
        UPDATE PictureEtag SET Etag = ? WHERE PictureId = ?
    """
    DELETE_PICTURE_ETAG_SQL = """
        DELETE FROM PictureEtag WHERE PictureId = ?
    """
    GET_PICTURE_ID_BY_ETAG = """
        SELECT PictureId FROM PictureEtag WHERE Etag = ?
    """

    GET_PICTURE_BINARY_SQL = """
        SELECT BinaryData FROM PictureBinary WHERE PictureId = ?
    """
    GET_PICTURE_ID_BY_BINARY_SQL = """
        SELECT PictureId FROM PictureBinary WHERE BinaryData LIKE ?
    """
    INSERT_PICTURE_BINARY_SQL = """
        INSERT INTO PictureBinary(PictureId, BinaryData)
            OUTPUT INSERTED.Id
        VALUES (?, ?)
    """
    UPDATE_PICTURE_BINARY_SQL = """
        UPDATE PictureBinary SET BinaryData = ? WHERE PictureId = ?
    """
    DELETE_PICTURE_BINARY_SQL = """
        DELETE FROM PictureBinary WHERE PictureId = ?
    """

    GET_PRODUCT_PACKAGE_UPC_BY_SKU = """
        SELECT Id
            ,Sku
            ,Product_Id
            ,Description
            ,Upc
        FROM Product_Package_Upc
        WHERE Sku = ?
    """


    
    DELETE_SPECIFICATION_ATTRIBUTE_BY_NAME_GROUPID_SQL = """
        DELETE FROM SpecificationAttribute
        WHERE Name = ? AND SpecificationAttributeGroupId = ?
    """

    DELETE_SPECIFICATION_ATTRIBUTE_BY_NAME_SQL = """
        DELETE FROM SpecificationAttribute
        WHERE Name = ? AND SpecificationAttributeGroupId IS NULL
    """

    DELETE_SPECIFICATION_ATTRIBUTE_OPTIONS_BY_SA_ID_SQL = """
        DELETE FROM SpecificationAttributeOption
        WHERE SpecificationAttributeId = ?
    """

    SAVE_SPECIFICATION_ATTRIBUTE_SQL = """
        DECLARE @Name nvarchar(max), @DisplayOrder int;

        SET @Name = ?;  
        SET @DisplayOrder = ?;
        
        IF EXISTS ( SELECT 1 FROM SpecificationAttribute WHERE UPPER(Name) = UPPER(@Name) )
            BEGIN
                SELECT Id, Name, DisplayOrder FROM SpecificationAttribute WHERE UPPER(Name) = UPPER(@Name)
            END
        ELSE
            BEGIN
                INSERT INTO SpecificationAttribute ( Name, DisplayOrder ) 
                OUTPUT INSERTED.* 
                VALUES (@Name, @DisplayOrder)
            END
    """

    SAVE_SPECIFICATION_ATTRIBUTE_OPTION_SQL = """
        DECLARE @Name nvarchar(max), @SpecId int, @DisplayOrder int;;
    
        SET @Name = ?;  
        SET @SpecId = ?;
        SET @DisplayOrder = ?;

        IF EXISTS ( SELECT 1 FROM SpecificationAttributeOption 
                    WHERE [Name] = @Name AND SpecificationAttributeId = @SpecId )
            BEGIN
                SELECT * FROM SpecificationAttributeOption 
                WHERE [Name] = @Name AND SpecificationAttributeId = @SpecId
            END
        ELSE	    
            BEGIN
                INSERT INTO SpecificationAttributeOption ( SpecificationAttributeId, [Name], DisplayOrder ) 
                OUTPUT INSERTED.* 
                VALUES (@SpecId, @Name, @DisplayOrder)
            END
    """
    
    SAVE_PRODUCT_SPECIFICATION_ATTRIBUTE_MAPPING_SQL = """
        DECLARE @SpecAttrOpId int, @ProductId int;
    
        SET @SpecAttrOpId = ?;  
        SET @ProductId = ?;

        IF EXISTS ( SELECT 1 FROM Product_SpecificationAttribute_Mapping 
                    WHERE SpecificationAttributeOptionId = @SpecAttrOpId AND ProductId = @ProductId )
            BEGIN
                SELECT * FROM Product_SpecificationAttribute_Mapping 
                WHERE SpecificationAttributeOptionId = @SpecAttrOpId AND ProductId = @ProductId
            END
        ELSE    
            BEGIN
            INSERT INTO Product_SpecificationAttribute_Mapping ( 
                    ProductId, 
                    AttributeTypeId, 
                    SpecificationAttributeOptionId, 
                    AllowFiltering, 
                    ShowOnProductPage, 
                    DisplayOrder 
                )
                OUTPUT INSERTED.* 
                VALUES (@ProductId, 0, @SpecAttrOpId, 0, 1, 0)
            END        
    """
    
    SAVE_PRODUCT_SPECIFICATION_ATTRIBUTE_MAPPING_V2_SQL = """
        DECLARE @ProductId int, @AttributeTypeId int, @SpecAttrOpId int, @AllowFiltering int, @ShowOnProductPage int, @DisplayOrder int;
            
        SET @ProductId = ?;
        SET @AttributeTypeId = ?;
        SET @SpecAttrOpId = ?;  
        SET @AllowFiltering = ?;
        SET @ShowOnProductPage = ?;
        SET @DisplayOrder = ?;

        IF EXISTS ( SELECT 1 FROM Product_SpecificationAttribute_Mapping 
                    WHERE SpecificationAttributeOptionId = @SpecAttrOpId AND ProductId = @ProductId )
            BEGIN
                SELECT * FROM Product_SpecificationAttribute_Mapping 
                WHERE SpecificationAttributeOptionId = @SpecAttrOpId AND ProductId = @ProductId
            END
        ELSE    
            BEGIN
            INSERT INTO Product_SpecificationAttribute_Mapping ( 
                    ProductId, 
                    AttributeTypeId, 
                    SpecificationAttributeOptionId, 
                    AllowFiltering, 
                    ShowOnProductPage, 
                    DisplayOrder 
                )
                OUTPUT INSERTED.* 
                VALUES (@ProductId, @AttributeTypeId, @SpecAttrOpId, @AllowFiltering, @ShowOnProductPage, @DisplayOrder)
            END        
    """

    GET_PRODUCT_SPECIFICATION_ATTRIBUTE_MAPPING_SQL = """
        SELECT * FROM Product_SpecificationAttribute_Mapping 
        WHERE SpecificationAttributeOptionId = @SpecAttrOpId
    """