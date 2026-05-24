# ==================== 1. 函数定义部分 ====================

def add_setting(settings_dict, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, key):
    key = key.lower()
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in settings_dict.items():
            result += f"{key.capitalize()}: {value}\n"
        return result

# ==================== 2. 测试和运行部分 ====================
if __name__ == "__main__":
    # 创建初始化字典
    test_settings = {
        'theme': 'dark',
        'notifications': 'enabled',
        'volume': 'high'
    }

    print("--- 初始设置 ---")
    print(view_settings(test_settings))

    print("--- 测试添加新设置 ---")
    print(add_setting(test_settings, ('language', 'English')))

    print("\n--- 最终设置内容 ---")
    print(view_settings(test_settings))
