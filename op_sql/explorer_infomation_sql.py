from basic_sql_op import op_database as opsql
import random

'''
英灵探索功能
input:英灵id,
output:按照json格式返回返回英灵地域，原型，起源，还有相关的百科，文章，书籍信息。
'''
def explorer_infomation(id):
    db=opsql.Database()
    dic_info = {}
    big_sql = "select region_name,origin_name,prototype_name,region_id,origin_id,prototype_id from explorer_infomation1 where servent_id=%s;"
    res = db.select(big_sql,[id])
    region_res = list(set([i[0] for i in res]))
    origin_res = list(set([i[1] for i in res]))
    prototype_res = list(set([i[2] for i in res]))
    dic_info["region"] = region_res[random.randint(0, len(region_res) - 1)]
    dic_info["origin"] = origin_res[random.randint(0, len(origin_res) - 1)]
    dic_info["prototype"] = prototype_res[random.randint(0, len(prototype_res) - 1)]
    region_id=list(set([i[3] for i in res]))[0]
    origin_id=list(set([i[4] for i in res]))[0]
    prototype_id=list(set([i[5] for i in res]))[0]
    dic_info['pedias'] =[]
    pedias_sql="select p.pedia_id,pedia_name,pedia_url from pedia p " \
               "inner join pedia_name pn on p.pedia_id=pn.pedia_id " \
               "where prototype_id=%s;"
    pedias_res=db.select(pedias_sql, [prototype_id])
    for i in pedias_res:
        pedias_dic={}
        pedias_dic['pedia_id']=i[0]
        pedias_dic['pedia_name'] = i[1]
        pedias_dic['pedia_url'] = i[2]
        dic_info['pedias'].append(pedias_dic)
    print(region_id)
    print(origin_id)
    print(prototype_id)
    dic_info['articles'] =[]
    articles_sql = "select a.article_id,article_title,article_content,author_name from article a " \
                   "left join region_and_article raa on raa.article_id=a.article_id " \
                   "left join origin_and_article oaa on oaa.article_id=a.article_id " \
                   "left join author_and_article aaa on a.article_id = aaa.article_id " \
                   "inner join author a2 on aaa.author_id = a2.author_id " \
                   "where region_id=%s or origin_id=%s"
    articles_res = db.select(articles_sql, [region_id,origin_id])
    for i in articles_res:
        articles_dic = {}
        articles_dic['article_id'] = i[0]
        articles_dic['article_title'] = i[1]
        articles_dic['article_content'] = i[2].replace('\n','')
        articles_dic['author'] = i[3]
        dic_info['articles'].append(articles_dic)

    dic_info['books'] =[]
    books_sql = "select book_name,isbn,writer_name from book b " \
                "inner join book_and_writer baw on b.book_id=baw.book_id " \
                "inner join writer w on w.writer_id=baw.writer_id" \
                " where b.book_id in " \
                "(select region_and_book.book_id from region_and_book where region_id=%s " \
                "union " \
                "select origin_and_book.book_id from origin_and_book where origin_id=%s);"
    books_res = db.select(books_sql, [region_id,origin_id])
    for i in books_res:
        books_dic = {}
        books_dic['book_title'] = i[0]
        books_dic['isbn_code'] = i[1]
        books_dic['book_writer'] = i[2]
        dic_info['books'].append(books_dic)
    db.close()
    return dic_info
