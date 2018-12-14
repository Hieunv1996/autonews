using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace AutoNewsWebsite
{
    public partial class _Default : Page
    {
        SqlDataAdapter dadapter;
        DataSet dset;
        PagedDataSource adsource;
        string connstring = "Data Source=DESKTOP-LM8I71M;Initial Catalog=AutoNews;Integrated Security=True";
        public int pos, totalPage;

        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                this.ViewState["vs"] = 0;
            }
            pos = (int)this.ViewState["vs"];
            DataListBind();
        }

        void DataListBind()
        {
            dadapter = new SqlDataAdapter("SELECT * FROM NEWS ORDER BY CreateDate DESC", connstring);
            dset = new DataSet();
            adsource = new PagedDataSource();
            dadapter.Fill(dset);
            adsource.DataSource = dset.Tables[0].DefaultView;
            adsource.PageSize = 5;
            adsource.AllowPaging = true;
            adsource.CurrentPageIndex = pos;
            totalPage = adsource.PageCount;
            btnprevious.Enabled = !adsource.IsFirstPage;
            btnnext.Enabled = !adsource.IsLastPage;
            DataList1.DataSource = adsource;
            DataList1.DataBind();
        }

        protected void btnprevious_Click(object sender, EventArgs e)
        {
            pos = (int)this.ViewState["vs"];
            pos -= 1;
            this.ViewState["vs"] = pos;
            DataListBind();
        }

        protected void btnnext_Click(object sender, EventArgs e)
        {
            pos = (int)this.ViewState["vs"];
            pos += 1;
            this.ViewState["vs"] = pos;
            DataListBind();
        }
    }
}