import itertools

def generate_ecom_titles(brand, core_keywords, modifiers, max_length=255):
    """
    电商标题堆叠优化工具 (适用于 Lazada 和 TikTok)
    通过对核心词和修饰词进行去重和排列组合，生成最大化搜索曝光的堆叠标题。
    """
    optimized_titles = []
    
    # 清洗和去重输入词
    core_keywords = list(dict.fromkeys([k.strip() for k in core_keywords if k.strip()]))
    modifiers = list(dict.fromkeys([m.strip() for m in modifiers if m.strip()]))
    
    # 生成不同的修饰词组合
    for r in range(1, min(4, len(modifiers) + 1)):
        for mod_comb in itertools.permutations(modifiers, r):
            # 构建基础标题：品牌名 + 核心词 + 修饰词堆叠
            title_parts = [brand] + core_keywords + list(mod_comb)
            full_title = " ".join(title_parts)
            
            # 严格控制电商平台标题字符长度
            if len(full_title) <= max_length and full_title not in optimized_titles:
                optimized_titles.append(full_title)
                
    return optimized_titles

if __name__ == "__main__":
    # 示例：汽车美容类目产品
    MY_BRAND = "Rayhong"
    CORE_WORDS = ["Car Ceramic Coating", "Liquid Hydrophobic Coat", "Auto Detail Spray"]
    MODIFIERS = ["High Gloss", "Scratch Repair", "Waterproof Quick Coat", "Philippines Stock"]
    
    print("--- 正在为 Lazada/TikTok 优化生成堆叠标题 ---")
    results = generate_ecom_titles(MY_BRAND, CORE_WORDS, MODIFIERS)
    
    for idx, title in enumerate(results[:5], 1):
        print(f"推荐标题 {idx}: {title}")
