using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace AutoNewsWebsite
{
    public partial class News : System.Web.UI.Page
    {
        public NewsObj detailNews = new NewsObj();
        public string newsBody;
        SqlDataProvider sql = new SqlDataProvider();
        protected void Page_Load(object sender, EventArgs e)
        {
           LoadDetailNews();
        }

        void LoadDetailNews()
        {
            string ID = Request.QueryString["ID"];
            var dt = sql.GetData("SELECT * FROM NEWS WHERE ID = '" + ID + "'").Rows[0];
            detailNews.Body = (string)dt["Body"];
            detailNews.Title = (string)dt["Title"];
            detailNews.Url = (string)dt["Url"];
            detailNews.Site = (string)dt["Site"];
            detailNews.Description = (string)dt["Description"];
            detailNews.ShortBody = (string)dt["ShortBody"];
            newsBody = detailNews.ShortBody;
            detailNews.CreateDate = ((DateTime)dt["CreateDate"]).ToString();
            detailNews.Id = dt["ID"].ToString();
        }

        public string GetLastestNews(int num)
        {
            string str = "<div style=\"marg\">";
            var dt = sql.GetData("SELECT TOP(" + num.ToString() + ") * FROM NEWS WHERE ID != '" + detailNews.Id + "' ORDER BY CreateDate DESC");
            for(int i = 0; i < dt.Rows.Count; i++)
            {
                str += "<p><a href=\"News.aspx?ID=" + dt.Rows[i]["ID"] + "\">" + (string)dt.Rows[i]["Title"] + "</a></p>";
            }
            return str;
        }

        protected void readFullNews_Click(object sender, EventArgs e)
        {
            if(readFullNews.Text.Equals("Xem bài báo gốc"))
            {
                newsBody = detailNews.Body;
                readFullNews.Text = "Xem bài báo tóm tắt";
            }
            else
            {
                newsBody = detailNews.ShortBody;
                readFullNews.Text = "Xem bài báo gốc";
            }
        }

        protected string LoadBody()
        {
            return newsBody;
        }
    }
}