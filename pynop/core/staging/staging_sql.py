from pynop.core.db import Query


class StagingQuery(Query):

    INSERT_STA_PRODUCT_RAW_SQL = """
        INSERT INTO [dbo].[erp_product_raw]
            ([ITEM_NUMBER]
            ,[DESCRIPTION]
            ,[UNIT_OF_MEASURE]
            ,[UNIT_COST]
            ,[PRODUCT_TYPE]
            ,[DEPARTMENT]
            ,[SELL_PRICE]
            ,[LIST_PRICE]
            ,[UPS_FLAG]
            ,[INSTOCK_FLG]
            ,[WEB_PRICE]
            ,[SECOND_DESC_SIZE]
            ,[STATUS_CODE]
            ,[DIST_CODE]
            ,[UNI_PRICE_CODE]
            ,[MODEL]
            ,[MISC_LINE_INFO]
            ,[HEADER_FACT_CODE]
            ,[WITH_FLAG]
            ,[EXPECTED_DATE]
            ,[WEIGHT]
            ,[DEPTH]
            ,[WIDTH]
            ,[HEIGHT]
            ,[CART_PRICE]
            ,[BRAND_DESC]
            ,[KEY_UPC_BARCODE])
        VALUES
            (?
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
            ,?)
    """

    INSERT_STA_PRODUCT_SQL = """
        INSERT INTO [dbo].[erp_product]
            ([ItemNumber]
            ,[Name]
            ,[ShortDescription]
            ,[Color]
            ,[OnAbcSite]
            ,[OnHawthorneSite]
            ,[OnAbcClearanceSite]
            ,[OnHawthorneClearanceSite]
            ,[Sku]
            ,[ManufacturerNumber]
            ,[DisableBuying]
            ,[Weight]
            ,[Length]
            ,[Width]
            ,[Height]
            ,[AllowInStorePickup]
            ,[InstockFlag]
            ,[IsNew]
            ,[NewExpectedDate]
            ,[LimitedStockDate]
            ,[BasePrice]
            ,[DisplayPrice]
            ,[CartPrice]
            ,[UsePairPricing]
            ,[PriceBucketCode]
            ,[CanUseUps]
            ,[CustomerEntersPrice]
            ,[Upc]
            ,[FactTag])
        VALUES
            (?
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
            ,?)
    """

    UPDATE_STA_PRODUCT_PRICE_SQL = """
        UPDATE [dbo].[erp_product]
        SET [BasePrice] = ?
            ,[DisplayPrice] = ?
            ,[CartPrice] = ?
            ,[UsePairPricing] = ?
            ,[PriceBucketCode] = ?
        WHERE [ItemNumber] = ?
    """
    INSERT_STA_PR_FILE_DISCOUNTS_SQL = """
        INSERT INTO [dbo].[erp_pr_file_discounts]
                ([ProductSku]
                ,[IsAbcDiscount]
                ,[IsHawthorneDiscount]
                ,[Name]
                ,[DiscountAmount]
                ,[StartDate]
                ,[EndDate])
            VALUES
                (?
                ,?
                ,?
                ,?
                ,?
                ,?
                ,?)
    """

    INSERT_STA_ACCESSORY_SQL = """
        INSERT INTO [dbo].[erp_accessory]
            ([ItemNumber]
            ,[AccessoryItemNumber])
        VALUES
            (?
            ,?)
    """

    INSERT_STA_MANUFACTURER_SQL = """
        INSERT INTO [dbo].[erp_manufacturer]
            ([BrandCode]
            ,[Name]
            ,[OnAbcSite]
            ,[OnHawthorneSite]
            ,[OnAbcClearanceSite]
            ,[OnHawthorneClearanceSite])
        VALUES
            (?
            ,?
            ,?
            ,?
            ,?
            ,?)
    """
    INSERT_STA_PRODUCT_MANUFACTURER_MAPPING_SQL = """
        INSERT INTO [dbo].[erp_product_manufacturer_mapping]
            ([ItemSku]
            ,[BrandCode])
        VALUES
            (?
            ,?)
    """

    INSERT_STA_PRODUCT_CATEGORY_MAPPING_SQL = """
        INSERT INTO [dbo].[erp_product_category_mapping]
            ([ItemSku]
            ,[CategoryAbcId])
        VALUES
            (?
            ,?)
    """

    INSERT_STA_SCANDOWN_DATE_SQL = """
        INSERT INTO [dbo].[erp_scandown_date]
            ([Sku]
            ,[Vend_Markdown]
            ,[Comm_Markdown]
            ,[Sale_Markdown]
            ,[StartDate]
            ,[EndDate])
        VALUES
            (?
            ,?
            ,?
            ,?
            ,?
            ,?)
    """

    INSERT_STA_WARRANTY_GROUP_SQL = """
        INSERT INTO [dbo].[erp_warranty_group]
            ([WarrantyGroupCode]
            ,[Description])
        VALUES
            (?
            ,?)
    """

    INSERT_STA_WARRANTY_ITEM_SQL = """
        INSERT INTO [dbo].[erp_warranty_item]
            ([Name]
            ,[PriceAdjustment]
            ,[WarrantyGroupCode]
            ,[WarrantyItemSku])
        VALUES
            (?
            ,?
            ,?
            ,?)
    """

    INSERT_STA_PRODUCT_WARRANTY_MAPPING_SQL = """
        INSERT INTO [dbo].[erp_product_warranty_group_mapping]
            ([WarrantyGroupCode]
            ,[ProductSku])
        VALUES
            (?
            ,?)
    """

    GET_STA_ITEM_NUMBER_SQL = """
        SELECT  [ItemNumber]
        FROM [dbo].[erp_product]
    """
    GET_STA_ITEM_NUMBER_SKU_MAP_SQL = """
        SELECT  [ItemNumber],[Sku]
        FROM [dbo].[erp_product]
    """
    GET_STA_PRODUCT_SQL = """
        SELECT  [ItemNumber]
            ,[Name]
            ,[ShortDescription]
            ,[Color]
            ,[OnAbcSite]
            ,[OnHawthorneSite]
            ,[OnAbcClearanceSite]
            ,[OnHawthorneClearanceSite]
            ,[Sku]
            ,[ManufacturerNumber]
            ,[DisableBuying]
            ,[Weight]
            ,[Length]
            ,[Width]
            ,[Height]
            ,[AllowInStorePickup]
            ,[InstockFlag]
            ,[IsNew]
            ,[NewExpectedDate]
            ,[LimitedStockDate]
            ,[BasePrice]
            ,[DisplayPrice]
            ,[CartPrice]
            ,[UsePairPricing]
            ,[PriceBucketCode]
            ,[CanUseUps]
            ,[CustomerEntersPrice]
            ,[Upc]
            ,[FactTag]
        FROM [dbo].[erp_product]
    """

    GET_STA_PR_FILE_DISCOUNTS_SQL = """
        SELECT [Id] id
        ,[ProductSku] sku
        ,[IsAbcDiscount] is_abc_discount
        ,[IsHawthorneDiscount] is_haw_discount
        ,[Name] name
        ,[DiscountAmount] discount_amount
    FROM [dbo].[erp_pr_file_discounts]
    """

    GET_STA_ACCESSORY_SQL = """
        SELECT [Id] id
            ,[ItemNumber] item_number
            ,[AccessoryItemNumber] acc_item_number
        FROM [dbo].[erp_accessory]
    """

    GET_STA_MANUFACTURER_SQL = """
        SELECT [Id] id
        ,[BrandCode] brand_code
        ,[Name] name
        ,[OnAbcSite] on_abc_store
        ,[OnHawthorneSite] on_haw_store
        ,[OnAbcClearanceSite] on_abc_clearance_store
        ,[OnHawthorneClearanceSite] on_haw_clearance_store
        FROM [dbo].[erp_manufacturer]
    """

    GET_STA_PRODUCT_MANUFACTURER_MAPPING_SQL = """
        SELECT [ItemSku] item_sku
        ,[BrandCode] brand_code
        FROM [dbo].[erp_product_manufacturer_mapping]
    """

    GET_STA_PRODUCT_CATEGORY_MAPPING_SQL = """
        SELECT [Id] id
        ,[ItemSku] sku
        ,[CategoryAbcId] category_id
        FROM [dbo].[erp_product_category_mapping]
    """

    GET_STA_SCANDOWN_DATE_SQL = """
        SELECT [Id] id
        ,[Sku] sku
        ,[Vend_Markdown] vend_markdown
        ,[Comm_Markdown] comm_markdown
        ,[Sale_Markdown] sale_markdown
        ,[StartDate] start_date
        ,[EndDate] end_date
        FROM [dbo].[erp_scandown_date]
    """

    GET_STA_WARRANTY_GROUP_SQL = """
        SELECT [Id] id
        ,[WarrantyGroupCode] warranty_group_code
        ,[Description] warranty_group_description
        FROM [dbo].[erp_warranty_group]
    """

    GET_STA_WARRANTY_ITEM_SQL = """
        SELECT [Id] id
        ,[Name] name
        ,[PriceAdjustment] price
        ,[WarrantyGroupCode] warranty_group_code
        ,[WarrantyItemSku] item_number
        FROM [dbo].[erp_warranty_item]
    """

    GET_STA_PRODUCT_WARRANTY_GROUP_MAPPING_SQL = """
        SELECT [Id] id
        ,[WarrantyGroupCode] warranty_group_code
        ,[ProductSku] sku
        FROM [dbo].[erp_product_warranty_group_mapping]
    """

    INSERT_STA_ERP_PICTURE_SQL = """
        INSERT INTO [dbo].[erp_picture_info]
            ([seo_filename]
            ,[mime]
            ,[etag]
            ,[abc_status]
            ,[haw_status]
            ,[created_date]
            ,[updated_date])
        VALUES
            (?
            ,?
            ,?
            ,?
            ,?
            ,GETDATE()
            ,GETDATE())
    """
    GET_STA_ERP_PICTURE_BY_SEO_SQL = """
        SELECT [id]
        ,[seo_filename]
        ,[mime]
        ,[etag]
        ,[abc_status]
        ,[haw_status]
        ,[created_date]
        ,[updated_date]
        FROM [dbo].[erp_picture_info]
        WHERE seo_filename = ?
    """
    GET_STA_ERP_PICTURE_SQL = """
        SELECT [id]
        ,[seo_filename]
        ,[mime]
        ,[etag]
        ,[abc_status]
        ,[haw_status]
        ,[created_date]
        ,[updated_date]
        FROM [dbo].[erp_picture_info]
    """
    UPDATE_STA_ERP_PICTURE_STATUS_SQL = """
        UPDATE erp_picture_info 
        SET abc_status=?, haw_status=?,
            updated_date=GETDATE()
        WHERE id=?
    """
    UPDATE_STA_ERP_PICTURE_ABC_STATUS_SQL = """
        UPDATE erp_picture_info 
        SET abc_status=?,
            updated_date=GETDATE() 
        WHERE id=?
    """
    UPDATE_STA_ERP_PICTURE_HAW_STATUS_SQL = """
        UPDATE erp_picture_info 
        SET haw_status=?,
            updated_date=GETDATE() 
        WHERE id=?
    """
    UPDATE_STA_ERP_PICTURE_ETAG_STATUS_SQL = """
        UPDATE erp_picture_info 
        SET etag=?, abc_status=?, haw_status=?,
            updated_date=GETDATE()
        WHERE id=?
    """

    GET_STG_PRODUCT_PICTURE_MAPPINGS_BY_SKU_SQL = """
        SELECT [id]
            ,[sku]
            ,[stg_picture_id]
            ,[display_order]
            ,[nop_ppm_id]
        FROM [stg_product_picture_mapping]
        WHERE sku = ?
        ORDER BY display_order
    """

    GET_STA_NOP_CATEGORY_HASHMAP_SQL = "SELECT ISAM_Id As ErpCategoryId, Nop_Id As CategoryId FROM _{tbl_prefix}_erp_nop_category_mapping"

    GET_SOT_NOP_CATEGORY_HASHMAP_SQL = "SELECT SoT_Id As SotCategoryId, Nop_Id As CategoryId FROM SoTCategory_NopCategory"

    GET_CLEARANCE_ITEM_HASHTABLE_SQL = "SELECT Sku,Item_Number,ABC_Clearance,HAW_Clearance,ABC_Qty,HAW_Qty FROM _clearance_item"

    GET_MANUAL_UPDATE_SKU_SQL = "SELECT sku FROM _manual_update_sku_list"

    GET_SYNC_SETTINGS_SQL = "SELECT name, value FROM [dbo].[_sync_settings]"
