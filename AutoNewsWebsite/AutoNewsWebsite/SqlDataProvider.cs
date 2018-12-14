using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace AutoNewsWebsite
{
    public class SqlDataProvider
    {
        private static String strcon = "Data Source=DESKTOP-LM8I71M;Initial Catalog=AutoNews;Integrated Security=True";
        protected static SqlConnection conn;
        public SqlDataProvider()
        {
            if (conn == null) conn = new SqlConnection(strcon);
        }
        public SqlConnection openConnection()
        {
            if (conn.State == ConnectionState.Closed) conn.Open();
            return conn;
        }
        public bool closeConnection()
        {
            if (conn.State == ConnectionState.Open) conn.Close();
            return true;
        }

        public DataTable GetData(string sql)
        {
            return GetData(GetCommand(sql));
        }

        public DataTable GetData(SqlCommand cmd)
        {
            try
            {
                if (cmd.Connection == null) { cmd.Connection = openConnection(); }
                using (DataSet ds = new DataSet())
                {
                    using (SqlDataAdapter da = new SqlDataAdapter())
                    {
                        da.SelectCommand = cmd;
                        da.Fill(ds);
                        return ds.Tables[0];
                    }
                }
            }
            finally
            {

            }
        }

        public int ExecuteNonQuery(string sql)
        {
            return ExecuteNonQuery(GetCommand(sql));
        }

        public int ExecuteNonQuery(SqlCommand cmd)
        {
            int row = 0;
            try
            {
                if (cmd.Connection == null) { cmd.Connection = openConnection(); }
                row = (int)cmd.ExecuteNonQuery();
            }
            finally
            {

            }
            return row;
        }

        public object ExecuteScalar(string sql)
        {
            return ExecuteScalar(GetCommand(sql));
        }

        public object ExecuteScalar(SqlCommand cmd)
        {
            try
            {
                if (cmd.Connection == null) { cmd.Connection = openConnection(); }
                return cmd.ExecuteScalar();
            }
            finally
            {

            }
        }

        private SqlCommand GetCommand(string sql)
        {
            SqlCommand cmd = new SqlCommand(sql, openConnection());
            return cmd;
        }
    }

}