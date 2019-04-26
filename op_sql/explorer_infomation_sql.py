from op_sql import op_postgresql as opsql
import op_sql.conn_sql as c
import random
def explorer_infomation(id,conn_info=c.get_now_conn()):

    dic_info = {}
    big_sql = "select region_name,origin_name,prototype_name,region_id,origin_id,prototype_id from servent_prototype sp inner join prototype p on sp.prototype_id=p.prototype_id inner join prototype_origin po on sp.prototype_id=po.prototype_id inner join prototype_region pr on sp.prototype_id=pr.prototype_id inner join region r on pr.region_id=r.region_id inner join origin o on po.origin_id=o.origin_id where servent_id='%s'" % (
        id)
    res = [i for i in opsql.select(big_sql, conn_info)]
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
    pedias_sql="select p.pedia_id,pedia_name,pedia_url from pedia p inner join pedia_name pn on p.pedia_id=pn.pedia_id where prototype_id='%s'"%(prototype_id)
    pedias_res=[i for i in opsql.select(pedias_sql, conn_info)]
    for i in pedias_res:
        pedias_dic={}
        pedias_dic['pedia_id']=i[0]
        pedias_dic['pedia_name'] = i[1]
        pedias_dic['pedia_url:'] = i[2]
        dic_info['pedias'].append(pedias_dic)

    dic_info['articles'] =[]
    articles_sql = "select a.article_id,article_title,article_content,author_name from region_and_article raa inner join article a on raa.article_id=a.article_id inner join author_and_article aaa on a.article_id=aaa.article_id inner join author au on aaa.author_id=au.author_id where region_id='%s'" % (
        region_id)
    articles_res = [i for i in opsql.select(articles_sql, conn_info)]
    for i in articles_res:
        articles_dic = {}
        articles_dic['article_id'] = i[0]
        articles_dic['article_title'] = i[1]
        articles_dic['article_content:'] = i[2]
        articles_dic['author:'] = i[3]
        dic_info['articles'].append(articles_dic)

    dic_info['books'] =[]
    books_sql = "select book_name,isbn,writer_name from book b inner join book_and_writer baw on b.book_id=baw.book_id inner join writer w on w.writer_id=baw.writer_id where b.book_id in (select region_book.book_id from region_book where region_id='%s' union select origin_book.book_id from origin_book where origin_id='%s'"%(region_id,origin_id)
    books_res = [i for i in opsql.select(books_sql, conn_info)]
    for i in books_res:
        books_dic = {}
        books_dic['book_title'] = i[0]
        books_dic['isbn_code'] = i[1]
        books_dic['book_writer:'] = i[2]
        dic_info['articles'].append(books_dic)

    return dic_info

#print(name_search("兰陵王",c.conn2_info))