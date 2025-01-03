import fs from "fs";
import matter from "gray-matter";
import dotenv from "dotenv";

dotenv.config();

export const readArticle = async (id: string) => {

  const articlePath = `${process.env.PROJ_ROOT}/articles/${id}.md`;
  const file = fs.readFileSync(articlePath, "utf-8");

  const {data,content} = matter(file);

  return {data,content};
}