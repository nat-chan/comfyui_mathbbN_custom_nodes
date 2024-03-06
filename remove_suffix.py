#!/usr/bin/env python3

class RemoveSuffix:
    RETURN_TYPES = ("STRING", ) # 出力ノードのデータ型
    RETURN_NAMES = ("filename_prefix", ) # 出力ノード名
    FUNCTION = "run" # ノード実行時に呼ばれる関数名
    OUTPUT_NODE = False # 実行の進んでいく終端ノードとして扱うか
    CATEGORY = "mathbbN" # 左クリックしたときに出てくるカテゴリ

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "filename_text": ("STRING", {}),
            },
        }

    def run(self, filename_text: str) -> str:
        filename_prefix = ".".join(filename_text.split(".")[:-1])
        return (filename_prefix, )

NODE_CLASS_MAPPINGS = {
    "RemoveSuffix": RemoveSuffix,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RemoveSuffix": "RemoveSuffix",
}