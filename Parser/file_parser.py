import re, csv
from Parser import utf8_validator

# TEST variable
pre_processed_list = ['2712.csv', '2711.csv', '2708.csv', '2709.csv', '2714.csv', '2720.csv', '2723.csv', '2725.csv',
                      '2728.csv', '2733.csv', '2734.csv', '2737.csv', '2736.csv', '2741.csv', '2742.csv', '2743.csv',
                      '2745.csv', '2746.csv', '2747.csv', '2749.csv', '2750.csv', '2751.csv', '2753.csv', '2754.csv',
                      '2755.csv', '2757.csv', '2758.csv', '2760.csv', '2761.csv', '2762.csv', '2764.csv', '2765.csv',
                      '2766.csv', '2767.csv', '2768.csv', '2775.csv', '2776.csv', '2777.csv', '2778.csv', '2780.csv',
                      '2784.csv', '2791.csv', '2795.csv', '2796.csv', '2797.csv', '2800.csv', '2801.csv', '2802.csv',
                      '2803.csv', '2804.csv', '2807.csv', '2809.csv', '2810.csv', '2811.csv', '2812.csv', '2814.csv',
                      '2815.csv', '2816.csv', '2818.csv', '2822.csv', '2823.csv', '2826.csv', '2828.csv', '2830.csv',
                      '2831.csv', '2832.csv', '2834.csv', '2835.csv', '2838.csv', '2840.csv', '2842.csv', '2843.csv',
                      '2846.csv', '2847.csv', '2850.csv', '2851.csv', '2853.csv', '2854.csv', '2858.csv', '2859.csv',
                      '2860.csv', '2861.csv', '2862.csv', '2868.csv', '2873.csv', '2875.csv', '2877.csv', '2880.csv',
                      '2881.csv', '2882.csv', '2884.csv', '2887.csv', '2888.csv', '2893.csv', '2894.csv', '2897.csv',
                      '2899.csv', '2901.csv', '2902.csv', '2903.csv', '2905.csv', '2906.csv', '2908.csv', '2910.csv',
                      '2912.csv', '2913.csv', '2915.csv', '2918.csv', '2925.csv', '2926.csv', '2929.csv', '2931.csv',
                      '2934.csv', '2937.csv', '2938.csv', '2940.csv', '2941.csv', '2942.csv', '2944.csv', '2945.csv',
                      '2948.csv', '2951.csv', '2952.csv', '2955.csv', '2957.csv', '2959.csv', '2960.csv', '2962.csv',
                      '2963.csv', '2965.csv', '2966.csv', '2967.csv', '2968.csv', '2969.csv', '2971.csv', '2972.csv',
                      '2974.csv', '2975.csv', '2978.csv', '2981.csv', '2982.csv', '2983.csv', '2986.csv', '2988.csv',
                      '2992.csv', '2996.csv', '2997.csv', '2998.csv', '3001.csv', '3002.csv', '3003.csv', '3004.csv',
                      '3008.csv', '3009.csv', '3010.csv', '3012.csv', '3014.csv', '3015.csv', '3019.csv', '3022.csv',
                      '3023.csv', '3024.csv', '3025.csv', '3026.csv', '3027.csv', '3028.csv', '3029.csv', '3030.csv',
                      '3032.csv', '3034.csv', '3035.csv', '3036.csv', '3037.csv', '3038.csv', '3039.csv', '3040.csv',
                      '3041.csv', '3042.csv', '3043.csv', '3044.csv', '3045.csv', '3047.csv', '3048.csv', '3049.csv',
                      '3050.csv', '3051.csv', '3053.csv', '3054.csv', '3055.csv', '3056.csv', '3058.csv', '3060.csv',
                      '3059.csv', '3061.csv', '3062.csv', '3063.csv', '3064.csv', '3065.csv', '3066.csv', '3067.csv',
                      '3068.csv', '3069.csv', '3071.csv', '3072.csv', '3073.csv', '3074.csv', '3075.csv', '3077.csv',
                      '3078.csv', '3079.csv', '3080.csv', '3081.csv', '3083.csv', '3082.csv', '3084.csv', '3085.csv',
                      '3086.csv', '3087.csv', '3089.csv', '3090.csv', '3091.csv', '3092.csv', '3093.csv', '3094.csv',
                      '3095.csv', '3096.csv', '3097.csv', '3098.csv', '3099.csv', '3100.csv', '3101.csv', '3102.csv',
                      '3103.csv', '3104.csv', '3105.csv', '3106.csv', '3110.csv', '3112.csv', '3115.csv', '3116.csv',
                      '3117.csv', '3118.csv', '3119.csv', '3120.csv', '3121.csv', '3122.csv', '3125.csv', '3126.csv',
                      '3127.csv', '3128.csv', '3130.csv', '3131.csv', '3132.csv', '3135.csv', '3136.csv', '3137.csv',
                      '3138.csv', '3139.csv', '3140.csv', '3141.csv', '3142.csv', '3144.csv', '3145.csv', '3146.csv',
                      '3147.csv', '3148.csv', '3149.csv', '3150.csv', '3151.csv', '3152.csv', '3153.csv', '3154.csv',
                      '3155.csv', '3158.csv', '3159.csv', '3160.csv', '3161.csv', '3162.csv', '3163.csv', '3164.csv',
                      '3166.csv', '3167.csv', '3168.csv', '3169.csv', '3170.csv', '3172.csv', '3176.csv', '3177.csv',
                      '3178.csv', '3180.csv', '3181.csv', '3182.csv', '3184.csv', '3185.csv', '3187.csv', '3188.csv',
                      '3189.csv', '3190.csv', '3193.csv', '3195.csv', '3194.csv', '3198.csv', '3199.csv', '3200.csv',
                      '3201.csv', '3202.csv', '3203.csv', '3204.csv', '3205.csv', '3206.csv', '3207.csv', '3212.csv',
                      '3214.csv', '3215.csv', '3218.csv', '3219.csv', '3220.csv', '3224.csv', '3226.csv', '3271.csv',
                      '3334.csv', '3336.csv', '3337.csv', '3338.csv', '3340.csv', '3341.csv', '3342.csv', '3343.csv',
                      '3345.csv', '3346.csv', '3348.csv', '3347.csv', '3349.csv', '3353.csv', '3355.csv', '3356.csv',
                      '3357.csv', '3358.csv', '3360.csv', '3361.csv', '3362.csv', '3364.csv', '3365.csv', '3367.csv',
                      '3368.csv', '3369.csv', '3370.csv', '3371.csv', '3373.csv', '3374.csv', '3372.csv', '3375.csv',
                      '3377.csv', '3378.csv', '3381.csv', '3383.csv', '3385.csv', '3387.csv', '3388.csv', '3389.csv',
                      '3392.csv', '3394.csv', '3396.csv', '3398.csv', '3400.csv', '3403.csv', '3407.csv', '3410.csv',
                      '3414.csv', '3417.csv', '3421.csv', '3422.csv', '3424.csv', '3425.csv', '3426.csv', '3427.csv',
                      '3428.csv', '3429.csv', '3430.csv', '3435.csv', '3436.csv', '3437.csv', '3441.csv', '3442.csv',
                      '3445.csv', '3446.csv', '3447.csv', '3448.csv', '3449.csv', '3450.csv', '3451.csv', '3453.csv',
                      '3455.csv', '3457.csv', '3458.csv', '3459.csv', '3460.csv', '3461.csv', '3462.csv', '3463.csv',
                      '3464.csv', '3466.csv', '3467.csv', '3468.csv', '3469.csv', '3471.csv', '3470.csv', '3472.csv',
                      '3473.csv', '3474.csv', '3476.csv', '3477.csv', '3479.csv', '3482.csv', '3483.csv', '3486.csv',
                      '3487.csv', '3493.csv', '3492.csv', '3496.csv', '3502.csv', '3503.csv', '3505.csv', '3506.csv',
                      '3510.csv', '3511.csv', '3514.csv', '3515.csv', '3517.csv', '3518.csv', '3519.csv', '3520.csv',
                      '3522.csv', '3523.csv', '3525.csv', '3532.csv', '3534.csv', '3537.csv', '3538.csv', '3539.csv',
                      '3541.csv', '3545.csv', '3547.csv', '3548.csv', '3549.csv', '3550.csv', '3551.csv', '3553.csv',
                      '3554.csv', '3555.csv', '3556.csv', '3558.csv', '3559.csv', '3561.csv', '3563.csv', '3564.csv',
                      '3566.csv', '3569.csv', '3573.csv', '3575.csv', '3577.csv', '3579.csv', '3586.csv', '3587.csv',
                      '3588.csv', '3589.csv', '3590.csv', '3591.csv', '3592.csv', '3593.csv', '3594.csv', '3595.csv',
                      '3596.csv', '3597.csv', '3598.csv', '3599.csv', '3600.csv', '3601.csv', '3602.csv', '3603.csv',
                      '3604.csv', '3605.csv', '3606.csv', '3609.csv', '3608.csv', '3610.csv', '3611.csv', '3613.csv',
                      '3614.csv', '3615.csv', '3616.csv', '3618.csv', '3619.csv', '3620.csv', '3621.csv', '3622.csv',
                      '3623.csv', '3624.csv', '3625.csv', '3626.csv', '3627.csv', '3628.csv', '3629.csv', '3631.csv',
                      '3632.csv', '3633.csv', '3634.csv', '3635.csv', '3636.csv', '3637.csv', '3638.csv', '3639.csv',
                      '3640.csv', '3641.csv', '3642.csv', '3643.csv', '3644.csv', '3645.csv', '3646.csv', '3674.csv',
                      '3675.csv', '3676.csv', '3677.csv', '3678.csv', '3680.csv', '3681.csv', '3682.csv', '3683.csv',
                      '3684.csv', '3685.csv', '3688.csv', '3690.csv', '3691.csv', '3692.csv', '3693.csv', '3694.csv',
                      '3696.csv', '3697.csv', '3698.csv', '3699.csv', '3700.csv', '3701.csv', '3702.csv', '3703.csv',
                      '3704.csv', '3705.csv', '3709.csv', '3708.csv', '3710.csv', '3713.csv', '3714.csv', '3715.csv',
                      '3716.csv', '3718.csv', '3719.csv', '3721.csv', '3722.csv', '3723.csv', '3724.csv', '3725.csv',
                      '3728.csv', '3729.csv', '3730.csv', '3731.csv', '3733.csv', '3735.csv', '3736.csv', '3737.csv',
                      '3738.csv', '3739.csv', '3741.csv', '3742.csv', '3743.csv', '3744.csv', '3745.csv', '3746.csv',
                      '3747.csv']
# TEST variable

data_path = utf8_validator.file_dump_path


def regexer(row):
    sector_pattern = r'\^\w+'
    stock_pattern = r'\n\w+'

    #   match for sector, Sector examples: ^FINANCIAL ^HOLDING ^INDUSTRIAL
    sector_match = re.match(stock_pattern, row[0])

    #    match for stock, Stock examples: \nAUB \nTEL
    stock_match = re.match(stock_pattern, row[0])

    if bool(sector_match) is True:
        return 'sector'
    return 'stock'


def processor(pre_processed_list):
    for file in pre_processed_list:
        with open(f'{data_path}/{file}') as raw_stock_records:
            all_rows = csv.reader(raw_stock_records)
            for row in all_rows:
                print(row)


#### ALL PSEUDOCODE
#   Need regexer

# for_regex = regexer(row)
# sector_match =
# stock _match True
# if row starts with '^':
#		log.info(f'found sectoral data for Sector {row[0]}')
#			sector_data['name'] = row[0]
#				sector_data['date'] = row[1]
#					sector_data['open'] = row[2]#
#					sector_data['high'] = row[3]
#					sector_data['low'] = row[4]#
#					sector_data['close'] = row[5]
#				elif row starts with (\w+):#
#					log.info(f'found stock data for Symbol {row[0]}')
#					stock_data['symbol'] = row[0]
#					stock_data['date'] = row[1]
#					stock_data['open'] = row[2]
##					stock_data['low'] = row[4]
#					stock_data['close'] = row[5]
#					stock_data['volume'] = row[6]
#					stock_data['netforeign'] = row[7]

# mydict = {rows[0]: rows[1] for rows in all_rows}
# if row starts with '^':
#		print('Sector ID Identified: ')
#		print(f'{file}')
# print(mydict)
processor(pre_processed_list)
