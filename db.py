from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite データベースのセットアップ
DATABASE_URL = "sqlite:///mvp_pos_system.db"  # SQLiteを使用
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# データベースモデルの定義
Base = declarative_base()

class SimpleDrink(Base):
    __tablename__ = 'simple_drinks'
    id = Column(Integer, primary_key=True)
    barcode = Column(String, unique=True, nullable=False)  # バーコード
    name = Column(String, nullable=False)  # 商品名
    brand = Column(String, nullable=False)  # ブランド名
    size = Column(String, nullable=False)  # サイズ（350mlなど）
    price = Column(DECIMAL, nullable=False)  # 価格
    stock = Column(Integer, nullable=False)  # 在庫数

# テーブルを作成
Base.metadata.create_all(engine)

# 10種類の商品データを追加
def add_sample_drinks():
    drinks = [
        SimpleDrink(barcode="4902509124513", name="コカ・コーラ", brand="コカ・コーラ", size="350ml", price=130, stock=100),
        SimpleDrink(barcode="4902102111513", name="ペプシコーラ", brand="ペプシ", size="500ml", price=140, stock=80),
        SimpleDrink(barcode="4901777230058", name="キリンレモン", brand="キリン", size="500ml", price=120, stock=60),
        SimpleDrink(barcode="4901085197362", name="アサヒスーパードライ", brand="アサヒ", size="350ml", price=210, stock=50),
        SimpleDrink(barcode="4901777301239", name="午後の紅茶", brand="キリン", size="500ml", price=160, stock=40),
        SimpleDrink(barcode="4902102071435", name="CCレモン", brand="サントリー", size="350ml", price=140, stock=90),
        SimpleDrink(barcode="4902102071442", name="三ツ矢サイダー", brand="アサヒ", size="500ml", price=150, stock=70),
        SimpleDrink(barcode="4902509124520", name="ファンタ", brand="コカ・コーラ", size="350ml", price=130, stock=120),
        SimpleDrink(barcode="4902102111506", name="ペプシネックス", brand="ペプシ", size="500ml", price=140, stock=50),
        SimpleDrink(barcode="4901777301260", name="午後の紅茶レモン", brand="キリン", size="500ml", price=160, stock=30)
    ]
    session.add_all(drinks)
    session.commit()

# サンプルデータをデータベースに追加
add_sample_drinks()

# 登録されたデータを確認するためのクエリ
sample_drinks = session.query(SimpleDrink).all()

# 結果を出力
for drink in sample_drinks:
    print(f"ID: {drink.id}, バーコード: {drink.barcode}, 名前: {drink.name}, ブランド: {drink.brand}, サイズ: {drink.size}, 価格: {drink.price}, 在庫: {drink.stock}")
